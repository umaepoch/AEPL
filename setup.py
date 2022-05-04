# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in aepl/__init__.py
from aepl import __version__ as version

setup(
	name='aepl',
	version=version,
	description='AEPL',
	author='pavithra M R',
	author_email='pavithramr88@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
