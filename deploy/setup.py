from setuptools import setup
import sys

# General Setup
PIP_NAME = 'maci'
VERSION = f"{sys.argv[1]}"
CODE_AUTHOR = 'aaronater10'
AUTHOR_EMAIL = 'dev_admin@dunnts.com'
PROJECT_URL = 'https://github.com/aaronater10/maci'
MODULES_INSTALLED = [PIP_NAME]

# Descriptions
DESCRIPTION = 'The easy to use library for your data, configuration, and save files'
with open('./README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

# Remove Custom Args
sys.argv.remove(sys.argv[1])

# Main Setup Params
setup(
    name=PIP_NAME,
    version=VERSION,
    url=PROJECT_URL,
    author=CODE_AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    py_modules=MODULES_INSTALLED,
    packages=[PIP_NAME],
    package_dir={PIP_NAME: PIP_NAME},
    include_package_data=True,
    install_requires=["PyYAML >= 5.4.1"],
    keywords=[PIP_NAME, CODE_AUTHOR, 'python', 'py', 'config', 'file', 'export', 'parse', 'text file', 'cfg', 'conf', 'save file', 'config file', 'db', 'database', 'simple', 'configuration', 'alternative', 'safe', 'ini', 'json', 'xml', 'yml', 'data', 'import'],
    license = 'MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ]
)
