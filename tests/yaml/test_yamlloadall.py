# yamlloadall - Tests
from src import maci

test_file_path = './tests/test_files/yaml/'


################################################################
# TESTS

# 1. Import Yaml File = Import a sample yaml file and validate attribute is accessible
def test1_yamlloadall_file():
    file_to_import = '1_yamlloadall_import.yml'    
    filepath_to_import = test_file_path + file_to_import
    num_of_docs = 2

    yaml_imported = list(maci.yamlloadall(filepath_to_import))

    assert num_of_docs == len(yaml_imported)

    for yaml_doc in yaml_imported:
        if isinstance(yaml_doc, dict) and ('mysqldatabase' in yaml_doc):
            assert (yaml_doc['mysqldatabase']['port'] == 3012) and (isinstance(yaml_doc['mysqldatabase']['port'], int))
