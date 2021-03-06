# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "human_api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(name=NAME,
      version=VERSION,
      description="Human Protocol API",
      author_email="dev@hmt.ai",
      url="",
      keywords=["Swagger", "Human Protocol API"],
      install_requires=REQUIRES,
      packages=find_packages(),
      package_data={'': ['swagger/swagger.yaml']},
      include_package_data=True,
      entry_points={'console_scripts': ['human_api=human_api.__main__:main']},
      long_description="""\
    Rest interface to interact with the Human Protocol
    """)
