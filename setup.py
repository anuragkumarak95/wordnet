import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "wordnet",
    version = "0.0.1",
    author = "Anurag Kumar",
    author_email = "anuragkumarak95@gmail.com",
    description = ("An module to create network of words "
                                   "on bases of realtive sense under a corpus of document."),
    license = "GNU General Public License v3",
    keywords = "word network python twitter streaming data",
    url = "https://anuragkumarak95.github.io/wordnet/",
    packages=['wordnet','wordnet.bin','wordnet.models'],
    install_requires=['colorama'],
    long_description=None, #read('README') # add a  README file and update here..
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
