# To install fitgrid in development mode see
# kutaslab.github.io/fitgrid-dev-docs/contributing.html

from setuptools import find_packages, setup
from fitgrid import get_ver

__version__ = get_ver()


def readme():
    with open('README.md') as strm:
        return strm.read()


setup(
    name='fitgrid',
    version=get_ver(),
    description='Mass multiple regression manager',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Andrey Portnoy, Thomas P. Urbach',
    author_email='aportnoy@ucsd.edu, turbach@ucsd.edu',
    url='https://github.com/kutaslab/fitgrid',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Science/Research",
    ],
    packages=find_packages(exclude=['tests']),
)
