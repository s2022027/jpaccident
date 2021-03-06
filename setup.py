
import setuptools
import os

#from pathlib import Path
#this_directory = Path(__file__).parent
#long_description = (this_directory / "README.md").read_text()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jpaccident",
    version="0.0.1",
    author="Tsuyoshi Hine",
    author_email="tsuyoshi.h0920@gmail.com",
    description='Package for visualization of aggregate data on fatalities in traffic accidents',
    long_description=long_description,
    long_description_content_type="text/plain",
    
    #long_description=open(path.join(here, 'README.md'), encoding='utf-8').read().replace("\r", "")
    #long_description_content_type="text/markdown",
    
    url="https://github.com/s2022027/jpaccident",
    project_urls={
        "Bug Tracker": "https://github.com/s2022027/jpaccident",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['jpaccident'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'jpaccident = jpaccident:main'
        ]
    },
)
