'''Author Anurag Kumar 13 Sept, 2017

Module for creating a network of word entities(look @ models/word.py for entity details)
'''
from .models import Word
import pickle, sys, time
from .bin import paint
from datetime import datetime
# local vars
TAG = paint('WORDNET/','b')
__WRNT_FORMAT =  'wrnt'
__WRNG_FORMAT_MSG = TAG+'\'.wrnt\' file format is needed'


def generate_net(idf,tf_idf,dump_path=None):
    # error handling
    if dump_path and dump_path[-4:] != __WRNT_FORMAT: raise Exception(__WRNG_FORMAT_MSG)

    start_t = datetime.now()
    print(TAG,'Network Genertion initiated..')
    word_net = {} # list of word entities.
    
    #registering all word instances in a dict of network
    for k in idf:
        word_net[k] = Word(k)
    print(TAG,'word-network instances created..',datetime.now()-start_t)

    #TODO: code for going through all the tf_idf elements and finding backward links and forward links of every word in word_net.
    for docs in tf_idf:
        for word in docs:
            word_net[word].addtofrwrd_links(set(docs))
    print(TAG, 'word filled with their relative words(network generated)... ',datetime.now()-start_t)
    
    words = {}
    words_arr = []
    relatives = []
    i=0
    for word in word_net:
        words_arr.append(word)
        words[word] = i
        i+=1
    
    print(TAG, 'created words_arr for output...',datetime.now()-start_t)    
    
    # total = len(words)
    # i=0 # % counter var
    for word in word_net:
        #  # this print statement gives error in python 2.6,2.7,3.2. comment until compatible replacement found.
        # i+=1
        # print('\r'+TAG+' '+paint(str(int((i/total)*100)),'r')+'% completed...',end='')    
        relatives.append([words[w] for w in word_net[word].frwrd_links]) 
    print()
    print(TAG, 'created final relative-words list.. return ready.',datetime.now()-start_t)
    
    # Dump the generated lists if dump_path is given.
    if dump_path:
        pickle.dump((words_arr,relatives),open(dump_path,'wb'),protocol=pickle.HIGHEST_PROTOCOL)
        print(TAG,'word network dumped @',dump_path,datetime.now()-start_t)

    return words_arr,relatives


def retrieve_net(wrnt_path):
    if wrnt_path[-4:] != __WRNT_FORMAT: raise Exception(__WRNG_FORMAT_MSG)
    
    words_arr, relatives = pickle.load(open(wrnt_path,'rb'))
    word_net = {}
    for w,r in zip(words_arr,relatives):
        word_net[w] = Word(w,None,set(r))
    # deleting useless resources, for efficient memory usage.
    del words_arr
    del relatives
    return word_net