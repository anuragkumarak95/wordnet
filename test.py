'''@Author: Anurag Kumar(mailto:anuragkumarak95@gmail.com) 

Module made for the soul purpose of build testing and validation.

This module will test only the functionalities of tf_idf_generator.py and nn_words.py. twitter_streaming.py can't be tested without confidential credetials(config.py file, have a look @ /README.md for further queries).
'''
from bin.paint import paint
from nn_words import find_knn 
from tf_idf_generator import find_tf_idf

TAG=paint('TEST/','b')

out_dict = {
 'OUT_TRUE_1' : ['shade', 'fifth', 'Minseok', 'Rotarian', 'preformed', 'YoungMin', 'VietNam', 'payong', 'Croatia', 'porefessional']
,'OUT_TRUE_2' : ['surprise', 'Benefiting', 'benefitted', 'VISAKA', 'Promising', 'KAMEN', 'Ruler', 'Personalise', 'glock', 'Stocks']
,'OUT_TRUE_3' : ['haryana', 'delhi', 'india', 'includes', 'correct']
,'OUT_TRUE_4' : ['punjab', 'Whther', 'evergreen', 'haryana', 'victam', 'Sikhs', 'delhi', 'rocks', 'godmen']
,'OUT_TRUE_5' : ['neggie', 'lanny', 'quicky', 'jetpackers', 'shepherd', 'kline', 'schoolgirl', 'barbie', 'entirely', 'crussades']
}
def test(n,word):
    print(TAG,'Test #',n, 'word == ',word)
    _ ,tf_idf = find_tf_idf(file_names=['test/testdata'],prev_file_path=None)
    
    out = []
    for w in find_knn(tf_idf,word,rand_on=False):
        out.append(w)
    print(TAG,out)
    if sorted(out) != sorted(out_dict['OUT_TRUE_'+str(n)]): return 1
    
    return 0

if __name__=="__main__":
    test(1,'hello')
    test(2,'stock')
    test(3,'punjab')
    test(4,'india')
    test(5,'german')
