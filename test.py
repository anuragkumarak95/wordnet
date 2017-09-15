'''@Author: Anurag Kumar(mailto:anuragkumarak95@gmail.com) 

Module made for the soul purpose of build testing and validation.

This module will test only the functionalities of tf_idf_generator.py and nn_words.py. twitter_streaming.py can't be tested without confidential credetials(config.py file, have a look @ /README.md for further queries).
'''
import wordnet.bin.paint
from wordnet import * 
import unittest

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
    idf, tf_idf = find_tf_idf(['test/testdata'])
    

def test_nnwords(word):
    out = []
    for w in find_knn(tf_idf,word,rand_on=False):
        out.append(w)    
    return out

# unittest class for Testing.
class TestWordNet(unittest.TestCase):
    def test_nnwords_module(self):
        for i in range(1,5):
            self.assertEquals(
                sorted(test_nnwords(words[i-1])),
                sorted(out_dict['OUT_TRUE_'+str(i)])
            )

    def test_wordnet_module(self):
        w,r = generate_net(idf,tf_idf,'test/test.wrnt')
        with open('test/test.wrnt','rb') as f:
            a_w,a_r = pickle.load(f)
    
        self.assertEquals(a_w,w)
        self.assertEquals(a_r,r)

if __name__=="__main__":
    __init__()
    unittest.main()
