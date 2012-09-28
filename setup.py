#coding=utf-8
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="retry_on_exceptions",
    version="0.1",
    author="Flávio Juvenal",
    author_email="flaviojuvenal@gmail.com",
    description="Decorator for retrying a function N times "
                "in case some specified exception occurs. ",
    license="MIT License",
    keywords="decorator decorators retry exception",
    url="https://github.com/fjsj/retry_on_exceptions",
    packages=['retry'],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
