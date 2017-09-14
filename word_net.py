'''Author Anurag Kumar 13 Sept, 2017

Module for creating a network of word entities(look @ models/word.py for entity details)
'''
from models.word import Word
import pickle, sys, time
def generate_net(idf,tf_idf):
    word_net = {} # list of word entities.
    
    #registering all word instances in a dict of network
    for k,element in idf.items():
        word_net[k] = Word(k)


    #TODO: code for going through all the tf_idf elements and finding backward links and forward links of every word in word_net.
    for docs in tf_idf:
        for word in docs:
            word_net[word].addtofrwrd_links([w if w != word else None for w in docs])

    for _,word in word_net.items():
        if len(word.frwrd_links) != 0:
            print(word.w,' :: ',len(word.frwrd_links))
    pickle.dump(word_net,open('word_net.wrdnt','wb'),protocol=pickle.HIGHEST_PROTOCOL)

if __name__=='__main__':
    idf,tf_idf = pickle.load(open('loadouts/loadout.tfidfpkl','rb'))
    generate_net(idf,tf_idf)
