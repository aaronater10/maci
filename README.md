[![Docs](https://raw.githubusercontent.com/aaronater10/maci/1.0.0/ext/maci_cover.png)](https://docs.macilib.org/)

# maci
The easy to use library for data serialization

![maci-version](https://img.shields.io/pypi/v/maci.svg?label=maci&color=blue)
![maci-language-version](https://img.shields.io/badge/lang-v1.0.0-purple)
[![qa-testing](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml/badge.svg)](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml)
![coverage](https://img.shields.io/badge/coverage-100%25-red)
![py-versions](https://img.shields.io/badge/py_versions-3.7_%7C_3.8_%7C_3.9_%7C_3.10_%7C_3.11_%7C_3.12-%23FFD43B)

#

(pending updated description)

maci itself is a pure Python-based library

# tutorials & docs:
**quick start: [tutorial video](https://docs.macilib.org/watch/quick-start)**

**full tutorials: [all videos](https://docs.macilib.org/watch/full-training-series)**

**docs: [maci docs](https://docs.macilib.org/)**

**changelog: [update history](https://docs.macilib.org/updates/changelog)**


# install flavors

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

# basic usage
### maci

load maci data from file
```python
maci_data = maci.load('my.file')
```
load raw data from file
```python
raw_data = maci.loadraw('my.file')
```
load attributes names and their values back into object from file
```python
maci.loadattrs('my.file', my_obj)
```
load as dict data from file
```python
dict_data = maci.loaddict('my.file')
```
load maci data from string
```python
maci_data = maci.loadstr('string = "data"')
```
load as dict data from string
```python
dict_data = maci.loadstrdict('string = "data"')
```
dump data to file
```python
maci.dump('my.file', maci_data or dict_data or my_obj)
```
dump raw data to file
```python
maci.dumpraw('my.file', 'my data')
```
dump data to string
```python
str_data = maci.dumpstr(maci_data or dict_data or my_obj)
```
build maci data
```python
maci_data = maci.build()
maci_data.data1 = 'my data'
maci_data.data2 = [1,2,3]
maci_data.data3 = 1.0
```

### tools
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
# performance

Performance tests each library loading **100,000 lines of data** each in their natural usage

Tests are done by loading a file with 100 lines of data 1000 times with the proper file syntax for each library. You may also consider this test about loading 1000 files within the time taken as well

Results vary based on system spec, but you may simulate or prove the same difference in test results for your needs from the "perf" dir in this repo. Results below is running the test 3 times consecutively

**libs tested:** json, pyyaml, tomli, xmltodict, maci

---

**Notes**

*XML ElementTree type and INI Configparser tests were left out for now*

*pyyaml loads much faster using its c-based safe loader, but using the native methods/functions provided as tests for fairness and potential compatibility issues*


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
| 1st   | json |
| 2nd   | xmltodict |
| 3rd   | tomli |
| 4th   | maci |
| 5th   | pyyaml (4th if using c-loader) |

These are the current differences in results for maci compared to popular or modern libraries. Looking to continually improve maci's performance and update the results, but so far, not bad for pure python

# testing & release
A maci release is only deployed/released if all qa tests pass, and if the revision number is incremented.

All coverage testing must be at 100% or test pipeline will fail (badge is not auto-updated, and just indicates confidence in testing at 100%).

# previous project support
Project maci is derived from an older project called [sfcparse](https://github.com/aaronater10/sfcparse) that is no longer supported, and still provides forward ported support for most of the older API names as a courtesy. sfcparse uses the MIT license, and therefore, maci does not really need to associate itself with that older project, but out of notice for the reason of having the forward ported support is it being mentioned if desiring to migrate.

Reason for sfcparse's deprecation was merely for desire of re-branding and scrapping the old to make usage simpler and anew, thus, maci.

Though maci does support the older API names as a courtesy, some names being attempted to use may throw exceptions. Also, functionality in a lot of the forward connected API names may require different parameter positional args or kwargs. See these files for API matched names and where they point to

function names: [\_\_init\_\_.py](https://github.com/aaronater10/maci/blob/main/src/maci/__init__.py) under \_\_getattr\_\_

exception names: [error.py](https://github.com/aaronater10/maci/blob/main/src/maci/error.py) under \_\_getattr\_\_