# setup.py

from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
    ],
)
