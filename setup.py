#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION='0.0.7'

setup(name='isub',
	version=VERSION,
	description='A tool for running scripts on an OpenShift cluster',
	url='http://github.com/dhruvkp090/isub',
	author='Jake Lever',
	author_email='dhruvk090@gmail.com',
	license='MIT',
	packages=['isub'],
	install_requires=[],
	include_package_data=True,
	entry_points = {
		'console_scripts': ['isub=isub.main:main'],
	})

