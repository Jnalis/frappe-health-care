from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in health_care/__init__.py
from health_care import __version__ as version

setup(
	name="health_care",
	version=version,
	description="Heathcare App",
	author="Juve",
	author_email="health@health.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
