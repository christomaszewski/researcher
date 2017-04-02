import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "researcher",
    version = "0.0.1",
    author = "Christopher 'ckt' Tomaszewski",
    author_email = "christomaszewski@gmail.com",
    description = ("A small experiment management library"),
    license = "BSD",
    keywords = "experiments management execution",
    url = "https://github.com/christomaszewski/researcher.git",
    packages=['researcher', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)