#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='click-datetime',
    version='0.1',
    description='Datetime type support for click.',
    long_description=readme,
    author='Dawson Reid',
    author_email='dreid93@gmail.com',
    url='https://github.com/ddaws/click-datetime',
    license='MIT',
    packages=['click_datetime'],
    install_requires=[
        'click',
    ],
    extras_require={
        'dev': [
            'wheel',
        ]
    }
)
