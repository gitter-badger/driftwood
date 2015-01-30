from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "version"), "r") as version_handle:
    version = version_handle.read().strip()

setup(
	name = "driftwood",
	version = version,
	description = "A collection of python logging extensions",
	url = "https://github.com/HurricaneLabs/driftwood",
	author = "Colton Leekley-Winslow",
	author_email = "colton@hurricanelabs.com",
	package_dir = {"":"src"},
	packages = find_packages("src"),
    install_requires = ["mongoengine"],
    download_url = "https://github.com/HurricaneLabs/driftwood/tarball/{0}".format(version)
)

