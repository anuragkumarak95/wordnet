'''Author Anurag Kumar 13 Sept, 2017

Module for creating a network of word entities(look @ models/word.py for entity details)
'''
from .models import Word
import pickle, sys, time
from .bin import paint
from datetime import datetime

TAG = paint('WORDNET/','b')
def generate_net(idf,tf_idf,dump_path=None):
    start_t = datetime.now()
    print(TAG,'Network Genertion initiated..')
    word_net = {} # list of word entities.
    
    #registering all word instances in a dict of network
    for k,element in idf.items():
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
    for k,word in word_net.items():
        words_arr.append(k)
        words[k] = i
        i+=1
    
    print(TAG, 'created words_arr for output...',datetime.now()-start_t)    
    
    # total = len(words)
    # i=0 # % counter var
    for _,word in word_net.items():
        #  # this print statement gives error in python 2.6,2.7,3.2. comment until compatible replacement found.
        # i+=1
        # print('\r'+TAG+' '+paint(str(int((i/total)*100)),'r')+'% completed...',end='')    
        relatives.append([words[w] for w in word.frwrd_links]) 
    print()
    print(TAG, 'created final relative-words list.. return ready.',datetime.now()-start_t)
    
    # Dump the generated lists if dump_path is given.
    if dump_path:
        if dump_path[-4:] == 'wrnt':
            pickle.dump((words_arr,relatives),open(dump_path,'wb'),protocol=pickle.HIGHEST_PROTOCOL)
            print(TAG,'word network dumped @',dump_path,datetime.now()-start_t)
    
    return words_arr,relatives
