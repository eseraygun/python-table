# coding=utf-8

from distutils.core import setup
from table import __version__ as version

setup(
    name='table',
    version=version,
    py_modules=['table'],
    url='http://github.com/eseraygun/python-table',
    license='BSD (2-clause)',
    author='Eser Aygün',
    author_email='eser.aygun@gmail.com',
    description='Provides a two-dimensional table class with named rows and columns, and related I/O utilities.',
    requires=['numpy']
)
