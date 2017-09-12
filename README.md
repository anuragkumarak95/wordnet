# WordNet ![buid-status](https://travis-ci.org/anuragkumarak95/wordnet.svg?branch=master)
Create a Simple network of words related to each other using Twitter Streaming API.

`python3` is being used as per this release.

## requirements ( use pip3 )
run on bash '`$pip3 install -r requirements.txt`' @ root directory and you will be ready to go..

Three major parts are in this release.
1. `Streamer` : twitter_streaming.py
2. `TF-IDF` Gene : tf_idf_generator.py
3. `NN` words Gene : nn_words.py  

## Way to go :
1. Clone this repo and go to root-dir(wordnet), Create a config.py file with details mentioned below:
    ```python
    # Variables that contains the user credentials to access Twitter Streaming API 
    # this link will help you(http://socialmedia-class.org/twittertutorial.html)
    access_token = "xxx-xx-xxxx"
    access_token_secret = "xxxxx"
    consumer_key = "xxxxxx"
    consumer_secret = "xxxxxxxx"
    nn_window = 10 
    ```
2. run `Streamer` with an array of filter words that you want to fetch tweets on.
eg. `$python3 twitter_streaming.py hello hi hallo namaste > data_file.txt`
this will save a line by line words from tweets filtered according to words used as args in `data_file.txt`.

3.  run `TF-IDF GENE` for generating a TF-IDF file for further process.
eg. `$python3 tf_idf_generator.py -d path/`
this will generate a loadout.tfidfpkl file at the root dir.
note# [current release](https://github.com/anuragkumarak95/wordnet/releases/tag/v0.0.1-beta) is generating a very large file from this process. I am woring on it. :+1: 

4. run `NN Words Gene` for finally generating words that are relative to a specified word from given file.
eg. `$python3 nn_words.py -f loadout.tfidfpkl -w hello`
this will output a list of words nearly related to the `hello` word provided in the command by looking at the given `loadout.tfidfpkl` file.

> *Step 1, 2 & 3* are needed to be done once only, and repeat *Step 3* as you feel free.

#### Have fun...

Developed by -
[Anurag Kumar](https://github.com/anuragkumarak95)
