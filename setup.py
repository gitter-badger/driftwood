from setuptools import setup, find_packages
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "version"), "r") as version_handle:
    version = version_handle.read().strip()

readme_path = os.path.join(here, 'README.rst')
with open(readme_path, "r") as readme_handle:
    readme = readme_handle.read()

setup(
	name = "driftwood",
	version = version,
	description = "A collection of python logging extensions",
    long_description = readme,
	url = "https://github.com/HurricaneLabs/driftwood",
	author = "Colton Leekley-Winslow",
	author_email = "colton@hurricanelabs.com",
	package_dir = {"":"src"},
	packages = find_packages("src"),
    install_requires = ["mongoengine"],
)

