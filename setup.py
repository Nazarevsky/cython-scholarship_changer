from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Practise 1',
    ext_modules=cythonize("pract1.pyx"),
    zip_safe=False,
)