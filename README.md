[![Docs](https://raw.githubusercontent.com/aaronater10/maci/main/ext/maci_cover.png)](https://docs.macilib.org/)

# maci
A Python-Styled Serialization Language & Thin Wrapper Library 

![maci-version](https://img.shields.io/pypi/v/maci.svg?label=maci&color=blue)
![maci-language-version](https://img.shields.io/badge/lang-v1.0.0-purple)
[![qa-testing](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml/badge.svg)](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml)
![coverage](https://img.shields.io/badge/coverage-100%25-red)
![py-versions](https://img.shields.io/badge/py_versions-3.7_%7C_3.8_%7C_3.9_%7C_3.10_%7C_3.11_%7C_3.12-%23FFD43B)

#

maci is an easy to use library for data serialization. It can parse native python data types from any plain file, which is safer than using an executable .py file for your stored or configuration data. There are useful language features built-in like creating realistic constants for your name/value pairs by locking them, mapping a name to another to follow its value similar to a pointer, and much more.

Its focus is to reduce boilerplate by removing repetitive code implementation, like code written for common file handling, or common libraries used like JSON, YAML, TOML, etc. maci on its own is a pure Python-based library, and I've used variations of this library on projects for many companies and decided I wanted to make a robust and stable public version. It has made common needs less painful, and has solved simplicity in many ways. Hope it helps you

# 🎓 tutorials & docs:
**quick start: [tutorial video](https://docs.macilib.org/watch/quick-start)**

**full tutorials: [all videos](https://docs.macilib.org/watch/full-training-series)**

**docs: [maci docs](https://docs.macilib.org/)**

**changelog: [update history](https://docs.macilib.org/updates/changelog)**

**readme**
\
[installing](#-install-flavors)\
[basic usage: maci](#-basic-usage)\
[basic usage: thin libs](#-basic-usage-thin-libs)\
[exceptions, hints, and built-in tools](#-helpful-extras)\
[performance](#%EF%B8%8F-performance)\
[testing & release](#-testing--release)\
[previous support](#-previous-project-support)


# 🍨 install flavors

**full --> maci, standard library, and 3rd-party packages**
```bash
pip install maci
```
**standard lib --> maci and standard library based packages only**
```bash
pip install maci-std
```
**just maci --> maci package only**
```bash
pip install maci-only
```

[back to top](#maci)

# 📖 basic usage
### maci

Example file "my.file" with maci (Python-styled) data
```python
# Example maci data "my.file"
data1 = 'my data'
data2 = 1
data3 = [1,2,3]
data4 = {'k1': 1}
data5 = True
data6 = (1,2,3)
data7 = {1,2,3}
data8 = 1.0
data9 = None
data10 = b'\ndata\n'
```
#### Load
load maci data from file
```python
maci_data = maci.load('my.file')
maci_data.data1  # access data with attr name
```
load raw data from file
```python
raw_data = maci.loadraw('my.file')  # returns string (default)
```
load attributes names and their values back into your object from file
```python
maci.loadattrs('my.file', my_obj)  # loads in-place
my_obj.data4  # access data in your object with attr name
```
load as dict data from file
```python
dict_data = maci.loaddict('my.file')
dict_data['data3']  # access data as dict key name
```
load maci data from string
```python
maci_data = maci.loadstr('data1 = "data"')
maci_data.data1  # access data with attr name
```
load as dict data from string
```python
dict_data = maci.loadstrdict('data3 = "data"')
dict_data['data3']  # access data as dict key name
```

#### Dump
dump data to file from maci object, dict, or your own object with attrs
```python
maci.dump('my.file', maci_data or dict_data or my_obj)
# creates new file with data formatted as maci syntax
```
dump raw data to file
```python
maci.dumpraw('my.file', 'my data')
# creates new file with data raw as-is to file
```
dump data to string from maci object, dict, or your own object with attrs
```python
str_data = maci.dumpstr(maci_data or dict_data or my_obj)
# returns string with data formatted as maci syntax
```

#### Build
build maci data in code
```python
maci_data = maci.build()
maci_data.data1 = 'my data'
maci_data.data2 = [1,2,3]
maci_data.data3 = 1
maci_data.data4 = True
```
#### In-File Language Features
maci supports varying in-file features. Here are some examples using a file named "my.file":

Lock an attr from re-assignment using a lock glyph
```python
# Example maci data in "my.file"
data1 +l= 'my data'
```
Hard Lock an attr from re-assignment, deletion, and unlocking using a hard lock glyph
```python
# Example maci data in "my.file"
data1 +h= 'my data'
```
Reference and follow another attr's value with an attr (like a pointer) using a map glyph
```python
# Example maci data in "my.file"
data1 = 'my data'
data2 +m= data1
```
Date and time parsing
```python
# Example maci data in "my.file"
# Multiple options -> returns datetime, date, or time object
date_time1 = 2023-03-13 22:06:00
date_time2 = 2023-03-13 22:06:00.50
time_date1 = 22:06:00 2023-03-13
time_date2 = 22:06:00.50 2023-03-13
time1 = 22:06:00
time2 = 22:06:00.50
date = 2023-03-13
date_time_iso8601 = 2023-03-13T22:06:00
```

#### In-Code Language Features
The in-file language features can also be handled in code with a maci object
```python
maci_data.lock_attr('data1')
maci_data.hard_lock_attr('data2')
maci_data.map_attr('data3', 'data4')
```
You may unlock attrs, unmap attrs, and much more with a maci object

Note: if you dump your maci object back to a file, all language features will be retained and represented appropriately in the file

[back to top](#maci)

# 📖 basic usage: thin libs

### json -> based on [json standard library](https://docs.macilib.org/docs/json)
load json data from file
```python
data = maci.jsonload('file.json')
```
load json data from string
```python
data = maci.jsonloadstr('{"k1": "data"}')
```
dump python data to file as json data
```python
maci.jsondump('file.json', data)
```
dump data to string as json data
```python
json_data = maci.jsondumpstr(data)
```
### yaml -> based on [pyyaml framework](https://docs.macilib.org/docs/yaml)
load yaml data from file
```python
data = maci.yamlload('file.yaml')
```
load yaml data from string
```python
data = maci.yamlloadstr('k1: data')
```
dump python data to file as yaml data
```python
maci.yamldump('file.yaml', data)
```
dump data to string as yaml data
```python
yaml_data = maci.yamldumpstr(data)
```
There are also "loadall" and "dumpall" for multiple yaml docs in a file

### toml -> based on [tomli libraries](https://docs.macilib.org/docs/toml)
load toml data from file
```python
data = maci.tomlload('file.toml')
```
load toml data from string
```python
data = maci.tomlloadstr('data1 = "data1"')
```
dump python data to file as toml data
```python
maci.tomldump('file.toml', data)
```
dump data to string as toml data
```python
toml_data = maci.tomldumpstr(data)
```
### ini -> based on [configparser standard library](https://docs.macilib.org/docs/ini)
load ini data from file
```python
configparser_data = maci.iniload('file.ini')
```
dump configparser data to file as ini data
```python
maci.inidump('file.ini', configparser_data)
```
build ini data to configparser data automatically - learn more about [configparser objects](https://docs.python.org/3/library/configparser.html)
```python
configparser_data = maci.inibuildauto({'section1': {'k1': 'value1'}})
```
build configparser data manually - learn more about [configparser objects](https://docs.python.org/3/library/configparser.html)
```python
configparser_data = maci.inibuildmanual()
```

### xml -> based on [xmltodict module & xml etree from standard library](https://docs.macilib.org/docs/xml)
#### Dict (easiest)

load xml data from file as dict
```python
dict_data = maci.xmlloaddict('file.xml')
```
load xml data from string as dict
```python
dict_data = maci.xmlloadstrdict('<tag>data</tag>')
```
dump dict data to file as xml data
```python
maci.xmldumpdict('file.xml', dict_data)
```
dump dict data to string as xml data
```python
xml_data = maci.xmldumpstrdict(dict_data)
```
#### ElementTree - learn more about [element tree objects](https://docs.python.org/3/library/xml.etree.elementtree.html)
load xml data from file as element tree object
```python
et_data = maci.xmlload('file.xml')
```
load xml data from string as element tree object
```python
et_data = maci.xmlloadstr('<tag>data</tag>')
```
dump element tree data to file as xml data
```python
maci.xmldump('file.xml', et_data)
```
dump element tree data to string as xml data
```python
xml_data = maci.xmldumpstr(et_data)
```
build element tree data manually
```python
et_data = maci.xmlbuildmanual()
```

[back to top](#maci)

# 🪄 helpful extras
### exceptions
All exceptions/errors thrown by maci and its thin wrapper libraries are conveniently accessible here:
```python
maci.error
```
Examples of different load exceptions
```python
maci.error.Load
maci.error.JsonLoad
maci.error.YamlLoad
maci.error.TomlLoad
```
To catch/suppress all maci exceptions, use its base exception
```python
maci.error.MaciError
```
### hinting
For type hinting/annotation needs, you can conveniently access the respective object types here:
```python
maci.hint
```
Examples of different hint objects
```python
maci.hint.MaciDataObj
maci.hint.ConfigParser
maci.hint.ElementTree
maci.hint.Element
```
### useful tools
#### cleanformat
format nested data cleanly 
```python
str_data = maci.cleanformat([1,{'k1': 1, 'k2': 2},2])

print(str_data)

Output -->
[
    1,
    {
        'k1': 1,
        'k2': 2,
    },
    2,
]
```
#### pickling
pickle your objects using a non-executable file concept with maci
```python
# Dump to file
maci_data.pickle_data = maci.pickledumpbytes(my_obj)
maci.dump('my.data', maci_data)

# Load back from file
maci_data = maci.load('my.data')
my_obj = maci.pickleloadbytes(maci_data.pickle_data)
```
This is better than having your whole file having the ability to be unpickled, especially if you cannot trust the file's integrity. More on this  from [python pickle docs](https://docs.python.org/3/library/pickle.html). Though this may help improve pickling needs, still use methods to verify integrity of your pickled data if required

#### hashing
Easily generate hash of a file and store hash - default hash is sha256
```python
maci.createfilehash('my.data', 'my.data.hashed')
# always returns string of file hash
```
Now simply compare the hash of the source file to check integrity when needed
```python
maci.comparefilehash('my.data', 'my.data.hashed')
# returns bool if hash is a valid match
```
Create hash of data - default hash is sha256
```python
maci.createhash('data')  # returns string of hash
```

[back to top](#maci)

# ⏳️ performance

Performance tests each library loading **100,000 lines of data** each in their natural usage

Tests are done by loading a file with 100 lines of data 1000 times with the proper file syntax for each library. You may also consider this test about loading 1000 files within the time taken as well

Results vary based on system spec, but you may simulate or prove the same difference in test results for your needs from the "perf" dir in this repo. Results below is running the test 3 times consecutively

**libs tested:** json, pyyaml, tomli, xmltodict, maci

---

**Notes**

*XML ElementTree type and INI Configparser tests were left out for now*

*pyyaml loads much faster using its c-based safe loader, but using the native out of the box methods/functions provided as tests for fairness and potential compatibility issues for needing LibYAML bindings*


---
[//]: <> (chose yml for nice color syntax)
```yml
# Test 1
$ python3 perf_load.py 
Performance tests: "load" - loading file 1000 times with 100 lines of data

xml: 0.225348
json: 0.016725
yaml: 3.625997
toml: 0.23937
maci: 0.807448

# Test 2
$ python3 perf_load.py 
Performance tests: "load" - loading file 1000 times with 100 lines of data

xml: 0.22595
json: 0.016566
yaml: 3.652053
toml: 0.242974
maci: 0.806545

# Test 3
$ python3 perf_load.py 
Performance tests: "load" - loading file 1000 times with 100 lines of data

xml: 0.225579
json: 0.01695
yaml: 3.611955
toml: 0.239593
maci: 0.802843
```

| place | lib |
| ----- | --- |
| 🥇 1st   | json - avg 0.016s |
| 🥈 2nd   | xmltodict - avg 0.225s |
| 🥉 3rd   | tomli - avg 0.240s |
| 4th   | maci - avg 0.805s |
| 5th   | pyyaml - avg 3.630s (4th if using CLoader) |

*Current differences in load time results for 100k lines of data from maci compared to popular or modern libraries*

Looking to continually improve maci's performance and update the results, but so far, not bad for pure python.

[back to top](#maci)

# 🚀 testing & release
### 300+ tests and counting ⚡️

A maci release is only deployed/released if all qa tests pass, and if the revision number is incremented.

All coverage testing must be at 100% or test pipeline will fail (badge is not auto-updated, and just indicates confidence in testing at 100%).

[back to top](#maci)

# ⏪ previous project support
Project maci is derived from an older project called [sfcparse](https://github.com/aaronater10/sfcparse) that is no longer supported, and still provides forward ported support for most of the older API names as a courtesy. sfcparse uses the MIT license, and therefore, maci does not really need to associate itself with that older project, but out of notice for the reason of having the forward ported support is it being mentioned if desiring to migrate.

Reason for sfcparse's deprecation was merely for desire of re-branding and scrapping the old to make usage simpler and anew, thus, maci.

Though maci does support the older API names as a courtesy, some names being attempted to use may throw exceptions. Also, functionality in a lot of the forward connected API names may require different parameter positional args or kwargs. See these files for API matched names and where they point to

function names: [\_\_init\_\_.py](https://github.com/aaronater10/maci/blob/main/src/maci/__init__.py) under \_\_getattr\_\_

exception names: [error.py](https://github.com/aaronater10/maci/blob/main/src/maci/error.py) under \_\_getattr\_\_

[back to top](#maci)