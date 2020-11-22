#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

setup(
    name='bioranges',
    version='0.0.1',
    author='Fyodor P. Goncharov',
    author_email='gfederix@gmail.com',
    license='LGPL v3.0 or later',
    install_requires=[
        'numpy',
        'pandas',
        'nptyping'
    ],
    extras_require={
        'tests': ['pytest']
    },
    packages=find_packages(exclude=('tests',)),
)
