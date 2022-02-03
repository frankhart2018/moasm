import os
import codecs
import pathlib
from setuptools import setup, find_packages
from distutils.dir_util import copy_tree

from moasm.utils.file_paths import MOASM_DIR

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

LIBS_DIR = os.path.join(os.path.curdir, "libs")


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def _post_install(setup):
    def _post_actions():
        copy_tree(LIBS_DIR, os.path.join(MOASM_DIR, "libs"))

    _post_actions()
    return setup


# This call to setup() does all the work
setup = _post_install(setup(
    name="moasm",
    version=get_version("moasm/__init__.py"),
    description="Low-level esoteric language",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/frankhart2018/moasm",
    author="Siddhartha Dhar Choudhury",
    author_email="sdharchou@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["moasm = moasm.run:run",]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
    ],
    # install_requires=["flask", "mypy"],
))