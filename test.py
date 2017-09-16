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
    global idf
    global tf_idf
    idf, tf_idf = find_tf_idf(['test/testdata'],None,'test/dump.tfidfpkl')
    
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
    
    def test_word(self):
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
        for i in range(1,5):
            self.assertEquals(
                sorted(test_nnwords(words[i-1])),
                sorted(out_dict['OUT_TRUE_'+str(i)])
            )
    
    # this function is  not working stable, 
    # it produces new list of words ,every time.
    # have a look at word_net.py, why is this happening.
    # and change dumpt_path=None after solution.
    def test_wordnet_module(self):
        # testing error raise code.
        wrng_name = 'test/test.wrng'
        with self.assertRaises(Exception): generate_net(idf,tf_idf,wrng_name)
        with self.assertRaises(Exception): retrieve_net(wrng_name)

        # WordNet Generate Net module walkthrough
        wrnt_name = 'test/test.wrnt'
        w,r = generate_net(idf,tf_idf)
        with open(wrnt_name,'rb') as f:
            a_w,a_r = pickle.load(f)
        
        # WordNet Reatrieval module walkthrough
        word_net = retrieve_net(wrnt_name)
        r_w=[]
        r_r=[]
        for word in word_net:
            r_w.append(word_net[word].w)
            r_r.append(word_net[word].frwrd_links)
    
        # only asserting length right now, as these process are not creating same sequence or words. check needed.
        self.assertEquals(len(a_w),len(w))
        self.assertEquals(len(a_r),len(r))
        self.assertEquals(len(a_w),len(r_w))
        self.assertEquals(len(a_r),len(r_r))

        # covering dump section of generate_net()
        generate_net(idf,tf_idf,wrnt_name)
        
        # cleaning as we move on!
        del a_w
        del a_r
        del r_w
        del r_r
        del w
        del r

if __name__=="__main__":
    __init__()
    unittest.main()
