#import setuptools
#import os
from setuptools import setup, find_packages
from codes import open
from os import path

def _requires_from_file(filename:str):
    return open(filename, encoding='utf-8').read().splitlines()

def _read_readme():
    return open(path.join(here, 'README.md'), encoding='utf-8').read().replace('\r','')

here = path.abspath(path.dirname(__file__))

#from pathlib import Path
#this_directory = Path(__file__).parent
#long_description = (this_directory / "README.md").read_text()


#with open("README.md", "r", encoding="utf-8") as fh:
 #   long_description = fh.read()

setup(
    name="jpaccident",
    version="0.0.1",
    author="Tsuyoshi Hine",
    author_email="tsuyoshi.h0920@gmail.com",
    description='Package for visualization of aggregate data on fatalities in traffic accidents',
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    long_description=_read_readme(),
    
    
    #long_description=open(path.join(here, 'README.md'), encoding='utf-8').read().replace("\r", "")
    long_description_content_type="text/markdown",
    
    url="https://github.com/s2022027/jpaccident",
    project_urls={
        "Bug Tracker": "https://github.com/s2022027/jpaccident",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #py_modules=['jpaccident'],
    #packages=setuptools.find_packages(where="src"),
    #python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'jpaccident = jpaccident:main'
        ]
    },
    include_package_data=True,
)
