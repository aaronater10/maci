# yamlload - Tests
from src import maci

test_file_path = './tests/test_files/yaml/'


################################################################
# TESTS

# 1. Import Yaml File = Import a sample yaml file and validate attribute is accessible
def test1_yaml_import_file():
    file_to_import = '1_yaml_import.yml'    
    filepath_to_import = test_file_path + file_to_import

    yaml_imported = maci.yamlload(filepath_to_import)
    assert (yaml_imported['mysqldatabase']['port'] == 3012) and (isinstance(yaml_imported['mysqldatabase']['port'], int))