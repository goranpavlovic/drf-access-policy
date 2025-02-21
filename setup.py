#!/usr/bin/env python
from codecs import open

from setuptools import setup


def readme():
    with open("README.md", "r") as infile:
        return infile.read()


classifiers = [
    # Pick your license as you wish (should match "license" above)
    "License :: OSI Approved :: MIT License",
    "Framework :: Django",
    "Framework :: Django :: 1.8",
    "Framework :: Django :: 1.9",
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Framework :: Django :: 3.0",
    "Framework :: Django :: 3.1",
    "Framework :: Django :: 3.2",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
setup(
    name="drf-access-policy",
    version="1.0.0",
    description="Declarative access policies/permissions modeled after AWS' IAM policies.",
    author="Robert Singer",
    author_email="robertgsinger@gmail.com",
    packages=["rest_access_policy"],
    url="https://github.com/rsinger86/drf-access-policy",
    license="MIT",
    keywords="django restframework drf access policy authorization declaritive",
    long_description=readme(),
    classifiers=classifiers,
    long_description_content_type="text/markdown",
    install_requires=["pyparsing", "djangorestframework"],
)
