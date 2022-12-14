from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    req = f.read().splitlines()

setup(
    name='master-thesis',
    version='1.0',
    description='',
    author_='Cezary Kręt',
    author_email='CezaryKret0@gmail.com',
    url='https://github.com/CezaryKretGit/Master-Thesis',
    packages=find_packages(exclude=('tests*', 'docs*', 'scripts*')),
    required=req
)