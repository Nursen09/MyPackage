from setuptools import setup, find_packages

setup(
    name = 'Mypackage',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'EDSA test package',
    long_description = open('readme.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/Nursen09/Mypackage',
    author = 'Nursen Naidoo',
    author_email = 'nursen.naidoo@gmail.com' 
)