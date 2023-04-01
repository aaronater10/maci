# tomlload - Tests
import datetime
from src import maci

test_file_path = './tests/test_files/toml/'


################################################################
# TESTS

# 1. TOML Load - Loading toml file data and test attributes
def test1_tomlload_file():
    filename = '1_load_data_file.toml'
    filepath = test_file_path + filename    

    # Test Data and it's Type
    toml_import = maci.tomlload(filepath)

    assert toml_import['title'] == "TOML Example"
    assert toml_import['owner'] == {'name': "Tom Preston-Werner", 'dob': datetime.datetime(1979, 5, 27, 7, 32, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600)))}
    assert toml_import['database'] == {
        'enabled': True,
        'ports': [8000, 8001, 8002],
        'data': [["delta", "phi"], [3.14]],
        'temp_targets': {'cpu': 79.5, 'case': 72.0}
    }
    assert toml_import['servers']['alpha'] == {'ip': "10.0.0.1", 'role': "frontend"}
    assert toml_import['servers']['beta'] == {'ip': "10.0.0.2", 'role': "backend"}
