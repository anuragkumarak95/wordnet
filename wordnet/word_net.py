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
    '''Generate WordNetwork dict of Word() instance, and dump as a file if asked to.

    @Args:
    --
    idf :       IDF value generated by find_tf_idf()
    tf_idf :    TF-IDF value generated by find_tf_idf()
    dump_path : file_path where to dump network entities, standart format is '.wrnt' (default=None)

    @returns:
    --
    word_net : list if Word() instances.(creating a network of words)
    '''
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
    
    # Dump the generated lists if dump_path is given.
    if dump_path:
        __words = {}
        __network = []
        i=0
        # creating word dict for refrence in next stage.
        for word in word_net:
            __words[word] = i
            i+=1
        # creating final network list to be dumped. format=['word',1,2,3,4...(refrences from words dict)]
        for word in word_net:   
            __temp_list = [word]
            __temp_list.extend([__words[w] for w in word_net[word].frwrd_links])
            __network.append(__temp_list)
            del __temp_list
        print(TAG, 'created final relative-words list.. return ready.',datetime.now()-start_t)
        # Dumping data using pickle
        pickle.dump(__network,open(dump_path,'wb'),protocol=pickle.HIGHEST_PROTOCOL)
        print(TAG,'word network dumped @',dump_path,datetime.now()-start_t)
        #cleaning afterwards
        del __words
        del __network

    return word_net


def retrieve_net(wrnt_path):
    '''Rerieves a dumped Network and generates WordNet instance.

    @Args:
    --
    wrnt_path : file_path to the '.wrnt' network dumped file.

    @returns:
    --
    word_net : dict of Word() entities generated from the input file.
    '''
    # Exception Handling of  wrong format.
    if wrnt_path[-4:] != __WRNT_FORMAT: raise Exception(__WRNG_FORMAT_MSG)
    
    file = open(wrnt_path,'rb')
    # retrieving a network  from .wrnt file.
    network = pickle.load(file)
    file.close()
    # Generating Word() instance dictionary from retrieved network.
    word_net = {}
    for n in network:
        word_net[n[0]] = Word(n[0],None,set(n[1:]))
    # deleting useless resources, for efficient memory usage.
    del network
    return word_net