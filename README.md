[![Docs](https://raw.githubusercontent.com/aaronater10/maci/1.0.0/ext/maci_cover.png)](https://docs.macilib.org/)

# maci
The easy to use library for data serialization

![maci-version](https://img.shields.io/pypi/v/maci.svg?label=maci&color=blue)
![maci-language-version](https://img.shields.io/badge/lang-v1.0.0-purple)
[![qa-testing](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml/badge.svg)](https://github.com/aaronater10/maci/actions/workflows/maci_qa.yml)
![coverage](https://img.shields.io/badge/coverage-100%25-red)
![py-versions](https://img.shields.io/badge/py_versions-3.7_%7C_3.8_%7C_3.9_%7C_3.10%7C_3.11-%23FFD43B)

#

(pending updated description)


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
# performance

Performance tests are loading a total of **100,000 lines of data** testing each library in their pure and natural use

Tests are done by loading a file with 100 lines of data 1000 times with the proper file syntax for each library. You may also consider this test about loading 1000 files within the time taken as well

Results vary based on system spec, but you may simulate or prove the same test results for your needs form the "perf" dir in this repo. Results below is running the test 3 times consecutively

**libs tested:** json, pyyaml, tomli, xmltodict, maci

# 

Notes:

- XML ElementTree type and INI Configparser tests were left out for now

- pyyaml loads much faster using it's c-based safe loader, but using the native methods/functions provided as tests for fairness



[//]: <> (chose yml for nice color syntax)
```yml
$ python3 perf_load.py 
Performance tests: "load" - loading file 1000 times with 100 lines of data

xml: 0.225348
json: 0.016725
yaml: 3.625997
toml: 0.23937
maci: 0.807448

$ python3 perf_load.py 
Performance tests: "load" - loading file 1000 times with 100 lines of data

xml: 0.22595
json: 0.016566
yaml: 3.652053
toml: 0.242974
maci: 0.806545

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

These are the current differences in results for maci compared to popular or modern libraries. Looking to continually improve it's performance and update the results, but so far, not bad

# testing & release
A maci release is only deployed/released if all qa tests pass, and if the revision number is incremented.

All coverage testing must be at 100% or test pipeline will fail (badge is not auto-updated, and just indicates confidence in testing at 100%).
