#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Install containment."""

from setuptools import find_packages, setup


setup(
    name="containment",
    author="Melissa Nuno",
    author_email="melissa@contains.io",
    license="MIT",
    url="https://github.com/contains-io/containment.git",
    use_scm_version=True,
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=[
        "docker-py >= 1.10.6, < 1.11",
        "jinja2 >= 2.8, < 3",
        "rcli >= 0.5, < 0.6",
    ],
    setup_requires=["pytest-runner", "rcli >= 0.5, < 0.6", "setuptools_scm"],
    tests_require=["pytest >= 5, < 6"],
    autodetect_commands=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
)
