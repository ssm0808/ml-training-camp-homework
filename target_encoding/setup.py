# coding:utf-8
# Author : Simon Shi
# FILE : setup.py
# DATE : 2021/5/1 14:12

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

compile_flags = ['-std=c++11',  '-fopenmp']
linker_flags = ['-fopenmp']

module = Extension('target_encoding_cython',
                   ['target_encoding_cython.pyx'],
                   language='c++',
                   include_dirs=[numpy.get_include()], # This helps to create numpy
                   extra_compile_args=compile_flags,
                   extra_link_args=linker_flags)

setup(
    name='target_encoding_cython',
    ext_modules=cythonize(module),
)


if __name__ == "__main__":
    pass

