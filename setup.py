#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_usersettings2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_usersettings2.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-usersettings2',
    version=version,
    description="""This package integrates django-usersettings2 with django-cms>=3.0, This allows a site editor to add/modify all usersettings in the frontend editing mode of django CMS and provide your users with a streamlined editing experience.""",
    long_description=readme + '\n\n' + history,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/djangocms-usersettings2',
    packages=[
        'djangocms_usersettings2',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms>=3.0',
        'django-usersettings2',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-usersettings2, site settings, django-cms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
