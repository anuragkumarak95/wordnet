'''@Author: Anurag Kumar(mailto:anuragkumarak95@gmail.com) 
This module takes a .tfidfpkl file generated by another module and a word for which it is suppose to process related words from that file, and output a specified amount of nearest neighbors.
'''
import datetime, os, pickle, argparse, operator
from colorama import Fore, Style
import config as cf
import random
TAG = Fore.BLUE+'NN_Words/'+Style.RESET_ALL

'''TODO-
1. (DONE)Start returning limited amount of neighbors.
2. (DONE)Arrange the returning word_bag on the bases of their tf-idf values for more sensible words to come up.
3. (DONE)create a part where input pickle file is verified for having intended data only, wrong file should not be parsed.
4. (DONE)create a structure where output is yielded but randomly some words are skipped to create unrecognizable patterns in output.
'''

def find_knn(tfidf_file_name,input_word,k=cf.nn_window):
    '''func that find k nearest neighbors of a spcified word from a given file of tf-idf values of words for list of docs.
    @Args:
    --
    tfidf_file_name : File name for the .tfidfpkl file to be used for searching.
    input_word : word for which process need to be done.
    k : amount of nearest neighbors to yield.(default=cf.nn_window)

    @yields:
    word : kth Nearnest Neighbor of the provided input_word for specified file.(generator yield)
    '''
    #load provided pickle file of list of dict about docs.
    tf_idf = pickle.load(open(tfidf_file_name,'rb'))

    #find docs that have imput_word and gather their content
    word_bag = {}
    for doc in tf_idf:
        contains_flag = False
        #print(doc)
        for word in doc:
            #print(word)
            if input_word == word:
                contains_flag = True
                break
        
        if contains_flag:
            #this code will only generate unique words and their tf_idf values, overwritten when already available..
            word_bag.update(doc)    
    #sort the availabel list of words from docs according to their tf_idf values.
    word_bag = sorted(word_bag.items(), key=operator.itemgetter(1))
    #reverse the order as to get words with large TF-IDF values(descending order)
    word_bag.reverse()
    for element,_ in zip(word_bag,range(k)):
        #condition where the word_bag throws the same word as input...(highly likely, hence ignored)
        if element[0] == input_word: continue
        if bool(random.getrandbits(1)): continue
        #creating a generator structure for better efficiency of code.
        yield element[0]

#func for implementing any prerocessing code.
def __init__():
    #code any initial passes here...
    pass

if __name__=='__main__':
    __init__()
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--tfidf", required=True, help="path to TF-IDF pickle file")
    ap.add_argument("-w","--word",required=True,help="Word for which nearest nieghbor is to be found from TF-IDF doc.")
    args = vars(ap.parse_args())
    tfidf_path = args['tfidf']
    word = args['word']
    
    #check if input is of write format...
    if tfidf_path[-8:] != 'tfidfpkl': 
        raise Exception(TAG+'Please provide a .tfidfpkl file that is generated by tf_idf_generator.py module...')
    out = []
    for word in find_knn(tfidf_path,word):
        out.append(word)
    print(TAG,out)
