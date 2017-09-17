__README_MD = 'README.md'
__README_RST = 'README.rst'


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


#converts markdown to reStructured
import pypandoc
z = pypandoc.convert(__README_MD,'rst',format='markdown')
#writes converted file
with open(__README_RST,'w') as outfile:
    outfile.write(z)


# script to run for pypi dist:
#   python setup.py sdist upload -r pypi
#   (for test) python setup.py sdist upload -r pypitest
from setuptools import setup
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
    install_requires=['colorama==0.3.9'],
    long_description=read(__README_RST),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

# remove converted file
os.remove(__README_RST)


