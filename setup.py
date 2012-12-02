# coding=utf-8

from distutils.core import setup
from table import __version__ as version

setup(
    name='table',
    version=version,
    py_modules=['table'],
    url='',
    license='BSD (2-clause)',
    author='Eser Aygün',
    author_email='eser.aygun@gmail.com',
    description='Provides a two-dimensional table class with named rows and columns, and related I/O utilities.',
    requires=['numpy']
)
