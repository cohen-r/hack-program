#! usr/bin/env python

from setuptools import setup

setup(
    name="compliments",
    version="0.0.1",
    packages=[],
    entry_points={
        'console_scripts': ['compliments = compliments.__main__:main']
    }
)