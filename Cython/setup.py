'''
Created on Aug 3, 2018

@author: thoma
'''
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello world app',
      ext_modules=cythonize("Hello.pyx"))