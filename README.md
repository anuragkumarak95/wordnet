# WordNet [![Build Status](https://travis-ci.org/anuragkumarak95/wordnet.svg?branch=master)](https://travis-ci.org/anuragkumarak95/wordnet)  [![codecov](https://codecov.io/gh/anuragkumarak95/wordnet/branch/master/graph/badge.svg)](https://codecov.io/gh/anuragkumarak95/wordnet)

Create a Simple network of words related to each other using Twitter Streaming API.

`python3` is being used as per this release.

## requirements ( use pip3 )

run on bash '`$pip3 install -r requirements.txt`' @ root directory and you will be ready to go..

Three major parts are in this project.

* `Streamer` : ~/twitter_streaming.py
* `TF-IDF` Gene : ~/wordnet/tf_idf_generator.py
* `NN` words Gene :~/ wordnet/nn_words.py

## Way to go

1. Clone this repo and go to root-dir(~), Create a config.py file with details mentioned below:
    ```python
    # Variables that contains the user credentials to access Twitter Streaming API
    # this link will help you(http://socialmedia-class.org/twittertutorial.html)
    access_token = "xxx-xx-xxxx"
    access_token_secret = "xxxxx"
    consumer_key = "xxxxxx"
    consumer_secret = "xxxxxxxx"
    ```
1. run `Streamer` with an array of filter words that you want to fetch tweets on. eg. `$python3 twitter_streaming.py hello hi hallo namaste > data_file.txt` this will save a line by line words from tweets filtered according to words used as args in `data_file.txt`.

1. To create a TF-IDF structure file for every doc, use:

    ```python
        from wordnet import find_tf_idf

        find_tf_idf(
            file_names=['file/path1','file/path2',..],    # paths of files to be processed.
            prev_file_path='prev/tf/idf/file/path',       # prev TF_IDF file to modify over.
            dump_path='path/to/dump/file'                 # dump_path if tf-idf needs to be dumped.
        )

        '''
        if no file is provided prev_file_path parameter, new TF-IDF file will be generated ,and else T
        F-IDF values will be combined with previous file, and dumped at dump_path if mentioned,
        else will only return the new tf-idf list of dictionaries.
        '''
    ```
1. To use `NN` Word Gene of this module, simply use wordnet.find_knn:

    ```python
    from wordnet import find_knn

    find_knn(
        tf_idf=tf_idf,       # this tf_idf is returned by find_tf_idf() above.
        input_word='german', # a word for which k nearest neighbours are required.
        k=10,                # k = number of neighbours required, default=10
        rand_on=True         # rand_on = either to randomly skip few words or show initial k words, default=True
    )

    '''
    This function will return a list of words closely related to provided input_word refering to tf_idf var provided to it. either use find_tf_idf() to gather this var or pickle.load() a dump
    file dumped by the same function at your choosen directory. the file contains 2 lists in format
    (idf, tf_idf).
    '''
    ```

1. To create a Word Network, use :

    ```python
    form wordnet import generate_net

    generate_net(
        idf=idf,                        # this tf_idf is returned by find_tf_idf() above.
        tf_idf=tf_idf,                  # this idf is returned by find_tf_idf() above.
        dump_path='path/to/dump.wrnt'   # dump_path = path to dump the generated files. default=None
    )

    '''
    this function returns 2 lists, which are (words_arr,relatives) where words_arr is list of unique words and realtives is a 2D array of indexes of those words representine a link between words.
    '''
    ```

### Test Run

To run a formal test, simply run this script. `python3 test.py`, this module will return **0** if everythinig worked as expected.

test.py uses sample data provided [here](./test/testdata) and executes tf_idf_generator.py & nn_words.py.

**Developed** with ![love](./icons/heart_min.png) by [@Anurag](https://github.com/anuragkumarak95)
