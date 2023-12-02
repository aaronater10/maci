# Internal File Versions - Tests
import subprocess
import json

################################################################
# Tests

# 1. Test File Versions on Required Files are Incremented - This ensures no new work can be done without incrementing app version
def test_file_version_check_is_incremented():
    # Setup
    file_versions_list = './tests/internal/file_versions.list'
    api_endpoint = 'https://pypi.org/pypi/maci/json'
    curl_request_cmd = ('curl', api_endpoint)

    # Collect Latest Package Release Number from PyPI API
    pkg_response_data = subprocess.run(curl_request_cmd, capture_output=True, text=True, check=True)
    latest_pkg_version = json.loads(pkg_response_data.stdout)['info']['version']

    possible_variations_found = (
        f"__version__ = '{latest_pkg_version}'",
        f"Version {latest_pkg_version}",
        f"MACI_VERSION = '{latest_pkg_version}'"
    )


    # Collect File Paths
    with open(file_versions_list, 'r') as file_data:
        list_of_file_paths = file_data.read().splitlines()

    # Tests
    for filepath in list_of_file_paths:
        # Skip comment lines or blanks
        if (filepath.startswith('#')) or (filepath.strip() == ''): continue

        # Check file for version match against latest pkg version
        with open(filepath, 'r') as version_file:
            version_file_data = version_file.read()
            for version_variation in possible_variations_found:
                if version_variation in version_file_data:
                    raise Exception(
                        f'Required file has old version in it not incremented to a newer revision!\nFile: {filepath} \nIncorrect version found inside: {latest_pkg_version} \nArea found: {version_variation}'
                    )
