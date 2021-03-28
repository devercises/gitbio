import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

entry_points = {
    'console_scripts': ['gitbio = gitbio.gitbio:main']
}

setup(
    name="gitbio",
    version="1.0.0",
    author="Devercises",
    description="project that shows your bio (or every person) from GitHub in CLI.",
    license="MIT",
    keywords=["github", "cli", "apis"],
    url="https://github.com/devercises/gitbio",
    packages=find_packages(),
    long_description=read("README.md")
)