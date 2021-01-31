#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='aaaaa',
    version="3.0.1",
    description="aaaa",
    author="aaaaaa",
    author_email="aaaaaaa",
    license='MIT',
    platforms=["OSX", "Windows", "Linux"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.pdf"]},
    install_requires=[
        "numpy", "scipy", "matplotlib", "scikit-learn", 'fire'
    ],
)