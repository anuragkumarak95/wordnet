'''@Author: Anurag Kumar(mailto:anuragkumarak95@gmail.com) 

Module made for the soul purpose of build testing and validation.

This module will test only the functionalities of tf_idf_generator.py and nn_words.py. twitter_streaming.py can't be tested without confidential credetials(config.py file, have a look @ /README.md for further queries).
'''
import wordnet.bin.paint
from wordnet import *
import unittest, os, pickle

TAG=paint('TEST/','b')
# test cases and var
words= ['hello','stock','punjab','india','german']
out_dict = {
 'OUT_TRUE_1' : ['shade', 'fifth', 'Minseok', 'Rotarian', 'preformed', 'YoungMin', 'VietNam', 'payong', 'Croatia', 'porefessional']
,'OUT_TRUE_2' : ['surprise', 'Benefiting', 'benefitted', 'VISAKA', 'Promising', 'KAMEN', 'Ruler', 'Personalise', 'glock', 'Stocks']
,'OUT_TRUE_3' : ['haryana', 'delhi', 'india', 'includes', 'correct']
,'OUT_TRUE_4' : ['punjab', 'Whther', 'evergreen', 'haryana', 'victam', 'Sikhs', 'delhi', 'rocks', 'godmen']
,'OUT_TRUE_5' : ['neggie', 'lanny', 'quicky', 'jetpackers', 'shepherd', 'kline', 'schoolgirl', 'barbie', 'entirely', 'crussades']
}
def __init__():
    # generating tf-idf from test/testdata file(default tf-idf file)
    global df
    global tf_idf
    df, tf_idf = find_tf_idf(['test/testdata'],None,'test/dump.tfidfpkl')
    
    # to cover find_tf_idf() lines that execute when prev_file is given.
    temp1,temp2 = find_tf_idf(['test/testdata'],'test/dump.tfidfpkl')
    del temp1
    del temp2
    os.remove('test/dump.tfidfpkl')
    
def test_nnwords(word):
    out = []
    for w in find_knn(tf_idf,word,rand_on=False):
        out.append(w)    
    return out

# unittest class for Testing.
class TestWordNet(unittest.TestCase):
    
    def test_Word_module(self):
        w1 = Word('test',set(['case']),set(['#1']))
        w2 = Word('test_new')
        w2.setw('test')
        w2.setbkwrd_links(set(['case']))
        w2.setfrwrd_links(set(['#2']))
        w2.addtobkwrd_links(set([]))
        w2.addtofrwrd_links(set([]))
        #assertions        
        self.assertEquals(w1.w,w2.getw())
        self.assertEquals(w1.bkwrd_links,w2.getbkwrd_links())
        self.assertFalse(w1.frwrd_links==w2.getfrwrd_links())
        #cleaning
        del w1
        del w2        
    
    def test_nnwords_module(self):
        for i in range(1,6):
            self.assertEquals(
                sorted(test_nnwords(words[i-1])),
                sorted(out_dict['OUT_TRUE_'+str(i)])
            )
    
    def test_wordnet_module(self):
        # testing error raise code.
        wrng_name = 'test/test.wrng'
        self.assertRaises(Exception, generate_net, (df,tf_idf,wrng_name))
        self.assertRaises(Exception, retrieve_net, (wrng_name))
        
        #test file
        wrnt_name = 'test/test.wrnt'
        # WordNet Reatrieve Net module walkthrough
        word_net_ret = retrieve_net(wrnt_name)
        # WordNet Generate Net module walkthrough
        word_net_gen = generate_net(df,tf_idf)
        
        # assertion or generated and retrived networks equality.    
        for word in word_net_gen:
            self.assertEquals(word_net_gen[word].w, word_net_ret[word].w)
            self.assertEquals(word_net_gen[word].frwrd_links, word_net_ret[word].frwrd_links)
        
        # test for return_net() func
        self.assertRaises(Exception, return_net  , ('rahim',word_net_gen,0))
        return_file = open('test/return_net_sample','rb')
        return_net_sample = pickle.load(return_file)
        return_file.close()
        self.assertEquals(sorted(return_net_sample),sorted(return_net('rahim',word_net_gen,depth=2)))
        
        # covering dump section of generate_net()
        generate_net(df,tf_idf,'test/dump.wrnt')
        
        # cleaning as we move on!
        os.remove('test/dump.wrnt')
        del word_net_gen
        del word_net_ret
        
if __name__=="__main__":
    __init__()
    unittest.main()
