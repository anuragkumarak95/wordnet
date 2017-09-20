# WordNet

[![Build Status](https://travis-ci.org/anuragkumarak95/wordnet.svg?branch=master)](https://travis-ci.org/anuragkumarak95/wordnet)
[![codecov](https://codecov.io/gh/anuragkumarak95/wordnet/branch/master/graph/badge.svg)](https://codecov.io/gh/anuragkumarak95/wordnet)
[![Requirements Status](https://requires.io/github/anuragkumarak95/wordnet/requirements.svg?branch=master)](https://requires.io/github/anuragkumarak95/wordnet/requirements/?branch=master)

Create a Simple **network of words** related to each other using **Twitter Streaming API**.

![Made with python-3.5](http://forthebadge.com/images/badges/made-with-python.svg)

Major parts of this project.

* `Streamer` : ~/twitter_streaming.py
* `TF-IDF` Gene : ~/wordnet/tf_idf_generator.py
* `NN` words Gene :~/ wordnet/nn_words.py
* `NETWORK` Gene : ~/wordnet/word_net.py

## Using Streamer Functionality

1. `Clone this repo` and run on bash '`$pip install -r requirements.txt`' @ root directory and you will be ready to go..

1. Go to root-dir(~), Create a config.py file with details mentioned below:
    ```python
    # Variables that contains the user credentials to access Twitter Streaming API
    # this link will help you(http://socialmedia-class.org/twittertutorial.html)
    access_token = "xxx-xx-xxxx"
    access_token_secret = "xxxxx"
    consumer_key = "xxxxxx"
    consumer_secret = "xxxxxxxx"
    ```
1. run `Streamer` with an array of filter words that you want to fetch tweets on. eg. `$python twitter_streaming.py hello hi hallo namaste > data_file.txt` this will save a line by line words from tweets filtered according to words used as args in `data_file.txt`.

## Using WordNet Module

1. `Clone this repo` and install wordnet module using this script,

        $python setup.py install

1. To create a `TF-IDF` structure file for every doc, use:

    ```python
    from wordnet import find_tf_idf

    df, tf_idf = find_tf_idf(
    file_names=['file/path1','file/path2',..],       # paths of files to be processed.(create using twitter_streamer.py)
    prev_file_path='prev/tf/idf/file/path.tfidfpkl', # prev TF_IDF file to modify over, format standard is .tfidfpkl. default = None
    dump_path='path/to/dump/file.tfidfpkl'           # dump_path if tf-idf needs to be dumped, format standard is .tfidfpkl. default = None
    )

    '''
    if no file is provided prev_file_path parameter, new TF-IDF file will be generated ,and else
    TF-IDF values will be combined with previous file, and dumped at dump_path if mentioned,
    else will only return the new tf-idf list of dictionaries, and df dictionary.
    '''
    ```
1. To use `NN` Word Gene of this module, simply use wordnet.find_knn:

    ```python
    from wordnet import find_knn

    words = find_knn(
    tf_idf=tf_idf,       # this tf_idf is returned by find_tf_idf() above.
    input_word='german', # a word for which k nearest neighbours are required.
    k=10,                # k = number of neighbours required, default=10
    rand_on=True         # rand_on = either to randomly skip few words or show initial k words default=True
    )

    '''
    This function will return a list of words closely related to provided input_word refering to
    tf_idf var provided to it. either use find_tf_idf() to gather this var or pickle.load() a dump
    file dumped by the same function at your choosen directory. the file contains 2 lists in format
    (idf, tf_idf).
    '''
    ```

1. To create a Word `Network`, use :

    ```python
    from wordnet import generate_net

    word_net = generate_net(
    df=df,                          # this df is returned by find_tf_idf() above.
    tf_idf=tf_idf,                  # this tf_idf is returned by find_tf_idf() above.
    dump_path='path/to/dump.wrnt'   # dump_path = path to dump the generated files, format standard is .wrnt. default=None
    )

    '''
    this function returns a dict of Word entities, with word as key.
    '''
    ```

1. To retrieve a Word `Network`, use :

    ```python
    from wordnet import retrieve_net

    word_net = retrieve_net(
        'path/to/network.wrnt' # path to network file, format standard is .wrnt.
        )
    '''
    this function returns a dictionary of Word entities, with word as key.
    '''
    ```

1. To retrieve list of words that are at some depth form a root word in the network, use:

    ```python
    from wordnet import return_net

    words = return_net(
        word,       # root word in this process.
        word_net,   # word network generated from generate_net()
        depth=1    # depth to which you wish this word collector to traverse.
    )
    '''
    This function returns a list of words that are at provided depth from root word in the
    network provided.
    '''
    ```

### Test Run

To run a formal test, simply run this script. `python test.py`, this module will return **0** if everythinig worked as expected.

test.py uses sample data provided [here](https://github.com/anuragkumarak95/wordnet/tree/master/test) and executes unittest on `find_tf_idf()`, `find_knn()` & `generate_net()`.

> `Streamer` functionality will not be provided under distribution of this code. That is just a script independent from the module.

#### Contributions Are welcomed here

![BUILT WITH LOVE](http://forthebadge.com/images/badges/built-with-love.svg)

by [@Anurag](https://github.com/anuragkumarak95)
