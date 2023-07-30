import sys
import os
import subprocess

# Setup
MACI_VERSIONS = {
    'current': "0.5.2",  # New/Current Version
    'previous': "0.5.1"  # Previous version release to New/Current one 
}
UPDATE_VERSION_FILES = ['README.md', 'src/maci/__init__.py']
DEPLOY_API_TOKEN = f"{sys.argv[1]}"
DEPLOY_SSH_KEY = f"{sys.argv[2]}"
USER_HOMEPATH = os.getenv('HOME')
USER_PYPI_CFG_FILE = f"{USER_HOMEPATH}/.pypirc"
PYPI_UNIQUE_ID = "__token__"
USER_GITHUB_CFG_FILE = f"{USER_HOMEPATH}/.gitconfig"
USER_SSH_KEY_FILE = f"{USER_HOMEPATH}/.ssh/id_ssh.deploy"
USER_SSH_CFG_FILE = f"{USER_HOMEPATH}/.ssh/config"
GITHUB_MACI_REPO = "git@github.com-maci:aaronater10/maci.git"

# Update Version in Files
def update_version_in_files(version_info: dict, file_list: list) -> None:
    for filepath in file_list:
        with open(filepath, 'r') as file:
            new_file_data = file.read().replace(version_info['previous'], version_info['current'])
        with open(filepath, 'w') as file:
            file.write(new_file_data)

update_version_in_files(MACI_VERSIONS, UPDATE_VERSION_FILES)


# Create SSH Path, Key File, and Set Permissions
subprocess.run(f'mkdir -p "{USER_HOMEPATH}/.ssh"', shell=True)
with open(USER_SSH_KEY_FILE, 'w') as f:
    f.write(DEPLOY_SSH_KEY)
    subprocess.run(f'chmod 600 "{USER_SSH_KEY_FILE}"', shell=True)

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

# Create PyPI Config File for API Auth
with open(USER_PYPI_CFG_FILE, 'w') as f:
    f.write(f"""[distutils]
index-servers =
    pypi
    maci

[pypi]
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}

[maci]
  repository = https://upload.pypi.org/legacy/
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}
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


# Attempt to Deploy, if ANY FAILURES, report and always remove API Token file
try:
    # Change to Deploy Dir
    os.chdir('deploy/')

    ### PYPI ###
    # Prep maci Files for Build
    subprocess.run("cp -f -r ../src/maci/ .", shell=True).check_returncode()
    subprocess.run("cp -f ../README.md .", shell=True).check_returncode()

    # Build Wheel from Setup, then Publish to PyPI
    subprocess.run(f"python3 -B setup.py {MACI_VERSIONS['current']} sdist bdist_wheel", shell=True).check_returncode()
    subprocess.run(f'python3 -B -m twine upload --repository "maci" dist/* --verbose', shell=True).check_returncode()
    print('SUCCESS: maci deployment')

    ### GITHUB ###
    # Clone and Tag New Release Number
    subprocess.run(f"git clone {GITHUB_MACI_REPO} ./maci_tag", shell=True).check_returncode()
    os.chdir('maci_tag/')
    subprocess.run(f"git tag v{MACI_VERSIONS['current']} -m 'Release v{MACI_VERSIONS['current']}'", shell=True).check_returncode()
    subprocess.run(f"git push origin v{MACI_VERSIONS['current']}", shell=True).check_returncode()
    os.chdir('..')
except BaseException as err_msg:
    print('FAILED: maci deployment step...')
    print(f'OUTPUT: {err_msg}')
finally:
    try:
        # Cleanup PyPI Config with API Token
        subprocess.run(f"rm -f {USER_PYPI_CFG_FILE}", shell=True).check_returncode()
        # Cleanup SSH Key File
        subprocess.run(f"rm -f {USER_SSH_KEY_FILE}", shell=True).check_returncode()
    except BaseException as err_msg:
        print('FAILED: CLEANUP step...')
        print(f'OUTPUT: {err_msg}')
