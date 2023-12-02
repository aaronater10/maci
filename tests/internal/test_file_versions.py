# Internal File Versions - Tests
import subprocess

################################################################
# Tests

# 1. Test File Versions on Required Files are Incremented - This ensures no new work can be done without incrementing app version
def test_file_version_check_is_incremented():
    # Setup
    file_versions_list = './tests/internal/file_versions.list'
    git_tag_cmd = ('git', 'tag', '-l')

    # Collect Latest Tag Number
    command_response = subprocess.run(git_tag_cmd, capture_output=True, text=True, check=True)
    latest_tag = command_response.stdout.splitlines()[-1].lstrip('v')
    possible_variations_found = (
        f"__version__ = '{latest_tag}'",
        f"Version {latest_tag}",
        f"MACI_VERSION = '{latest_tag}'"
    )


    # Collect File Paths
    with open(file_versions_list, 'r') as file_data:
        list_of_file_paths = file_data.read().splitlines()

    # Tests
    for filepath in list_of_file_paths:
        # Skip comment lines or blanks
        if (filepath.startswith('#')) or (filepath.strip() == ''): continue

        # Check file for version match against latest git tag
        with open(filepath, 'r') as version_file:
            version_file_data = version_file.read()
            for version_variation in possible_variations_found:
                if version_variation in version_file_data:
                    raise Exception(
                        f'Required file has old version in it not incremented to a newer revision!\nFile: {filepath} \nIncorrect version found inside: {latest_tag} \nArea found: {version_variation}'
                    )
