# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.mdO') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cf-helpers',
    version='0.1.0',
    description='Pyton helper for AWS CloudFormation',
    long_description=readme,
    author='Q.S. Wang',
    author_email='wangqs_eclipse@yahoo.com',
    url='https://github.com/qs-wang/cf-helpers',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)