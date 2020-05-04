####################################################################
#                                                                  #
# react-flask                                                      #
# Copyright (C) 2020, Vilhelm Prytz, <vilhelm@prytznet.se>, et al. #
#                                                                  #
# Licensed under the terms of the MIT license, see LICENSE.        #
# https://github.com/VilhelmPrytz/react-flask                      #
#                                                                  #
####################################################################

import sys
from setuptools import setup, find_packages
from react_flask.version import version

assert sys.version_info >= (3, 6, 0), "react-flask requires Python 3.6+"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="react-flask",
    version=version,
    author="Vilhelm Prytz",
    author_email="vlhelm@prytznet.se",
    description="Render React components from Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://react-flask.readthedocs.io",
    project_urls={
        "Documentation": "https://react-flask.readthedocs.io",
        "Code": "https://github.com/VilhelmPrytz/react-flask",
        "Issue tracker": "https://github.com/VilhelmPrytz/react-flask/issues",
    },
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
