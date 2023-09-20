import sys
import os
import subprocess
from glob import glob


# Setup
MACI_VERSION = '0.6.1'
UPDATE_VERSION_FILES = ['README.md', 'src/maci/__init__.py']
DEPLOY_TYPE = f"{sys.argv[1]}"
DEPLOY_API_TOKEN = f"{sys.argv[2]}"
DEPLOY_SSH_KEY = f"{sys.argv[3]}" if len(sys.argv) == 4 else None
USER_HOMEPATH = os.getenv('HOME')
USER_PYPI_CFG_FILE = f"{USER_HOMEPATH}/.pypirc"
PYPI_UNIQUE_ID = "__token__"
USER_GITHUB_CFG_FILE = f"{USER_HOMEPATH}/.gitconfig"
USER_SSH_KEY_FILE = f"{USER_HOMEPATH}/.ssh/id_ssh.deploy"
USER_SSH_CFG_FILE = f"{USER_HOMEPATH}/.ssh/config"
GITHUB_MACI_REPO = "git@github.com-maci:aaronater10/maci.git"
ignore_github_deploy_list = (
    'maci-std',
    'maci-only'
)


# Create SSH Path, Key File, and Set Permissions
if DEPLOY_SSH_KEY is not None:
    subprocess.run(('mkdir', '-p', f'{USER_HOMEPATH}/.ssh'))
    with open(USER_SSH_KEY_FILE, 'w') as f:
        f.write(DEPLOY_SSH_KEY)
        subprocess.run(('chmod', '600', USER_SSH_KEY_FILE))

    # Create SSH Config File for SSH Auth
    with open(USER_SSH_CFG_FILE, 'w') as f:
        f.write(
    f"""
    Host github.com-maci
        Hostname github.com
        IdentityFile {USER_SSH_KEY_FILE}
        IdentitiesOnly yes
    """
    )

    # Create GitHub Config File for SSH Auth
    with open(USER_GITHUB_CFG_FILE, 'w') as f:
        f.write(
    """[user]
        email = dev_admin@dunnts.com
        name = aaronater10

    [url "ssh://git@github.com/"]
        insteadOf = https://github.com/
    """
    )


# Create PyPI Config File for API Auth
with open(USER_PYPI_CFG_FILE, 'w') as f:
    f.write(f"""[distutils]
index-servers =
    pypi
    {DEPLOY_TYPE}

[pypi]
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}

[{DEPLOY_TYPE}]
  repository = https://upload.pypi.org/legacy/
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}
"""
)



# Attempt to Deploy, if ANY FAILURES, report and always remove secrets
try:
    # Change to Deploy Dir
    os.chdir('deploy/')

    
    ### PYPI ###

    # Prep core maci Files for Build
    subprocess.run(('cp', '-f', '-r', '../src/maci/', '.')).check_returncode()
    subprocess.run(('cp', '-f', '../README.md', '.')).check_returncode()

    # Prep: maci-std
    deploy_type_path = ''
    if DEPLOY_TYPE == 'maci-std':
        deploy_type_path = 'maci_std'
        subprocess.run(('cp', '-f', *glob(f'alt_dist/{deploy_type_path}/*.py*'), 'maci/')).check_returncode()
        subprocess.run(('cp', '-f', f'alt_dist/{deploy_type_path}/MANIFEST.in', f'alt_dist/{deploy_type_path}/setup.cfg', '.')).check_returncode()

    # Prep: maci-only
    if DEPLOY_TYPE == 'maci-only':
        deploy_type_path = 'maci_only'
        subprocess.run(('cp', '-f', *glob(f'alt_dist/{deploy_type_path}/*.py*'), 'maci/')).check_returncode()
        subprocess.run(('cp', '-f', f'alt_dist/{deploy_type_path}/MANIFEST.in', f'alt_dist/{deploy_type_path}/setup.cfg', '.')).check_returncode()


    # Build Wheel from Setup, then Publish to PyPI
    subprocess.run(('python3', '-B', 'setup.py', MACI_VERSION, 'sdist', 'bdist_wheel')).check_returncode()
    subprocess.run(('python3', '-B', '-m', 'twine', 'upload', '--repository', DEPLOY_TYPE, *glob('dist/*'), '--verbose')).check_returncode()
    print('SUCCESS: maci deployment')

    
    ### GITHUB ###

    # Clone and Tag New Release Number if required
    if DEPLOY_TYPE not in ignore_github_deploy_list:
        subprocess.run(('git', 'clone', GITHUB_MACI_REPO, './maci_tag')).check_returncode()
        os.chdir('maci_tag/')
        subprocess.run(('git', 'tag', f'v{MACI_VERSION}', '-m', f"Release v{MACI_VERSION}")).check_returncode()
        subprocess.run(('git', 'push', 'origin', f'v{MACI_VERSION}')).check_returncode()
        os.chdir('..')

    # Return to root code dir
    os.chdir('..')

except BaseException as err_msg:
    print('FAILED: maci deployment step...')
    raise SystemExit(f'OUTPUT: {err_msg}')  # exits 1

finally:
    try:
        # Cleanup PyPI Config with API Token
        subprocess.run(('rm', '-f', USER_PYPI_CFG_FILE)).check_returncode()
        # Cleanup SSH Key File
        subprocess.run(('rm', '-f', USER_SSH_KEY_FILE)).check_returncode()

    except BaseException as err_msg:
        print('FAILED: CLEANUP step...')
        print(f'OUTPUT: {err_msg}')
