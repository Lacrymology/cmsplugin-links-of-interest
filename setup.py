#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin-links-of-interest'
    version='0.1',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = ('django-cms plugin to maintain a Links of Interest list'),
    packages=find_packages(),
    provides=['cmsplugin_links_of_interest', ],
    include_package_data=True,
)
