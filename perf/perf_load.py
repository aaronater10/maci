# imports
import time
import json
import yaml
import tomli
import xmltodict
import maci

# setup
num_of_file_load_tests = 1_000
num_lines_of_data_in_file = 100
xml_file = 'perf.xml'
json_file = 'perf.json'
yaml_file = 'perf.yml'
toml_file = 'perf.toml'
maci_file = 'perf.data'

# run tests
print(f'Performance tests: "load" - loading file {num_of_file_load_tests} times with {num_lines_of_data_in_file} lines of data\n')

# XML
t1 = time.perf_counter()
for _ in range(num_of_file_load_tests):
    with open(xml_file, 'rb') as file_data:
        data = xmltodict.parse(file_data)
t2 = time.perf_counter()
print(f'xml: {round(t2-t1, 6)}')

# JSON
t1 = time.perf_counter()
for _ in range(num_of_file_load_tests):
    with open(json_file, 'r') as file_data:
        data = json.load(file_data)
t2 = time.perf_counter()
print(f'json: {round(t2-t1, 6)}')

# YAML
t1 = time.perf_counter()
for _ in range(num_of_file_load_tests):
    with open(yaml_file, 'r') as file_data:
        data = yaml.safe_load(file_data)
t2 = time.perf_counter()
print(f'yaml: {round(t2-t1, 6)}')

# TOML
t1 = time.perf_counter()
for _ in range(num_of_file_load_tests):
    with open(toml_file, 'rb') as file_data:
        data = tomli.load(file_data)
t2 = time.perf_counter()
print(f'toml: {round(t2-t1, 6)}')

# MACI
t1 = time.perf_counter()
for _ in range(num_of_file_load_tests):
    data = maci.load(maci_file)
t2 = time.perf_counter()
print(f'maci: {round(t2-t1, 6)}')
