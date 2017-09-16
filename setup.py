import os
from setuptools import setup
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# expects an installed pypandoc: pip install pypandoc
# from pypandoc.pandoc_download import download_pandoc
# # see the documentation how to customize the installation path
# # but be aware that you then need to include it in the `PATH`
# download_pandoc()
# #converts markdown to reStructured
# z = pypandoc.convert('README.md','rst',format='markdown')
# #writes converted file
# with open('README.rst','w') as outfile:
#     outfile.write(z)

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
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

# script to run for pypi dist:
#   python setup.py sdist upload -r pypi
#   (for test) python setup.py sdist upload -r pypitest
