#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

setup(
    name='bioranges',
    version='0.0.1',
    author='Fyodor P. Goncharov',
    author_email='gfederix@gmail.com',
    license='LGPL v3.0 or later',
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'nptyping',
        'typing',
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-mypy',
            'coverage',
            'pytest-cov',
            'pytest-mock'
        ]
    },
    packages=find_packages(exclude=('tests',)),
)
