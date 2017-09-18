# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),'Ur').read()
# retrieving current version from module.
exec(open('wordnet/__pkginfo__.py').read())

from setuptools import setup, find_packages
setup(
    name = "wordnet",
    version = __version__,
    author = "Anurag Kumar",
    author_email = "anuragkumarak95@gmail.com",
    description = ("An module to create network of words "
                                   "on bases of realtive sense under a corpus of document."),
    license = "GNU General Public License v3",
    keywords = "word network python twitter streaming data",
    url = "https://anuragkumarak95.github.io/wordnet/",
    packages=find_packages(),
    install_requires=['colorama==0.3.9'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python"
    ],
)