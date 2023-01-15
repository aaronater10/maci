from setuptools import setup
import sys

VERSION = f"{sys.argv[1]}"
# Remove Custom Args
sys.argv.remove(sys.argv[1])

# Run setup
setup(version=VERSION)
