"""Python setup.py for word_counter package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("word_counter", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="word_counter",
    version=read("word_counter", "VERSION"),
    description="A simple command-line tool that counts the number of words in a text file.",
    url="https://github.com/nogibjj/HugoHu-Script-Package",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Hugo Hu",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["word_counter = word_counter.__main__:main"]},
    extras_require={"test": read_requirements("requirements.txt")},
)
