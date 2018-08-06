'''
Created on 06.08.2018

@author: chou
'''
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Parameters',
      ext_modules=cythonize("Cython_Loop.pyx"))