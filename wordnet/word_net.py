'''Author Anurag Kumar 13 Sept, 2017

Module for creating a network of word entities(look @ models/word.py for entity details)
'''
from .models import Word
import pickle, sys, time
from .bin import paint

TAG = paint('WORDNET/','b')
def generate_net(idf,tf_idf,dump_path=None):
    word_net = {} # list of word entities.
    
    #registering all word instances in a dict of network
    for k,element in idf.items():
        word_net[k] = Word(k)


    #TODO: code for going through all the tf_idf elements and finding backward links and forward links of every word in word_net.
    for docs in tf_idf:
        for word in docs:
            word_net[word].addtofrwrd_links([w if w != word else None for w in docs])

    words = {}
    words_arr = []
    relatives = []
    i=0
    for k,word in word_net.items():
        words_arr.append(k)
        words[k] = i
        i+=1
    total = len(words)
    i=0 # % counter var
    for _,word in word_net.items():
        i+=1
        print('\r'+TAG+' '+paint(str((i/total)*100),'r')+'% completed...',end='')    
        relatives.append([words[w] if w else None for w in word.frwrd_links]) 
    print()
    # Dump the generated lists if dump_path is given.
    if dump_path:
        pickle.dump((words_arr,relatives),open(dump_path,'wb'),protocol=pickle.HIGHEST_PROTOCOL)
        print(TAG,'word network dumped @',dump_path)
    
    return words_arr,relatives
