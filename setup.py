#coding=utf-8
from setuptools import setup

setup(
    name="retry_on_exceptions",
    version="0.0.1",
    author="Flávio Juvenal",
    author_email="flaviojuvenal@gmail.com",
    description="Decorator for retrying a function N times "
                "in case some specified exception occurs. ",
    license="MIT License",
    keywords="decorator decorators retry exception",
    url="https://github.com/fjsj/retry_on_exceptions",
    packages=['retry'],
    long_description="Decorator for retrying a function N times by "
                     "catching one of the specified exceptions and then retrying. "
                     "Specially useful for functions that throws errors sporadically, "
                     "like ones that depends on external resources as web APIs, databases, etc.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
