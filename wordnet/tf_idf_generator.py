import datetime, os, math, argparse, pickle, glob
from colorama import Fore, Style
import pickle

from .bin import paint  #custom module for coloring different strings.
'''TO-DO
1. find a better way to dump tf-idf values, too much data being used for now using list of dict
2. try to find more efficient ways to compute and calculate TF-IDF values , loop reduction required.
3. (DONE)change this code to pick a path and create TF-IDF dump from content of all of those files, where every line behaves like a independent document.
4. introduce a progress rate or better yet progress bar to the output.
'''

TAG = paint('TF-IDF-GENE/','b')
def find_tf_idf(file_names=['./../test/testdata'],prev_file_path=None, dump_path=None):
    '''Function to create a TF-IDF list of dictionaries for a corpus of docs.

    @Args:
    --
    file_names : paths of files to be processed on, these files are created using twitter_streaming module.
    prev_file_path : path of old .tfidfpkl file, if available. (default=None)
    dump_path : directory-path where to dump generated lists.(default=None)

    @returns:
    --
    idf : a dict of unique words in corpus,with their document frequency as values.
    tf_idf : the generated tf-idf list of dictionaries for mentioned docs.
    '''
    tf_idf = [] # will hold a dict of word_count for every doc(line in a doc in this case)
    idf = {}

    # this statement is useful for altering existant tf-idf file and adding new docs in itself.(## memory is now the biggest issue)
    if prev_file_path:
        print(TAG,'modifying over exising file.. @',prev_file_path)
        idf,tf_idf = pickle.load(open(prev_file_path,'rb'))
        prev_doc_count = len(idf)
        prev_corpus_length = len(tf_idf)

    for f in file_names:

        file1 = open(f,'r') # never use 'rb' for textual data, it creates something like,  {b'line-inside-the-doc'}
        
        #create word_count dict for all docs
        for line in file1:
            dict = {}
            #find the amount of doc a word is in
            for i in set(line.split()):
                if i in idf: idf[i] +=1
                else: idf[i] =1
            for word in line.split():
                #find the count of all words in every doc
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
            tf_idf.append(dict)
        file1.close()

    #calculating final TF-IDF values  for all words in all docs(line in a doc in this case)
    for doc in tf_idf:
        for key in doc:
            true_idf = math.log(len(tf_idf)/idf[key])
            true_tf = doc[key]/len(doc)
            doc[key] = true_tf * true_idf

    print(TAG,'Total number of unique words in corpus',len(idf),'( '+paint('++'+str(len(idf)-prev_doc_count),'g')+' )' if prev_file_path else '')
    print(TAG,'Total number of docs in corpus:',len(tf_idf),'( '+paint('++'+str(len(tf_idf)-prev_corpus_length),'g')+' )' if prev_file_path else '')
    
    # dump if a dir-path is given
    if dump_path:
        pickle.dump((idf,tf_idf),dump_path+'loadout.tfidfpkl',protocol=pickle.HIGHEST_PROTOCOL)
    return idf,tf_idf

