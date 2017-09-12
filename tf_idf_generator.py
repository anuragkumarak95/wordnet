import datetime, os, math, argparse, pickle, glob
from colorama import Fore, Style
import pickle

from bin.paint import paint #custom module for coloring different strings.
'''TO-DO
1. find a better way to dump tf-idf values, too much data being used for now using list of dict
2. try to find more efficient ways to compute and calculate TF-IDF values , loop reduction required.
3. (DONE)change this code to pick a path and create TF-IDF dump from content of all of those files, where every line behaves like a independent document.
4. introduce a progress rate or better yet progress bar to the output.
'''

TAG = paint('TF-IDF-GENE/','b')
def find_tf_idf(file_names=['test.txt'],prev_file_path=None):
    tf_idf = [] # will hold a dict of word_count for every doc(line in a doc in this case)
    idf = {}

    # this statement is useful for altering existant tf-idf file and adding new docs in itself.(## memory is now the biggest issue)
    if prev_file_path:
        print(TAG,'modifying over exising file.. @',prev_file_path)
        idf,tf_idf = pickle.load(open(prev_file_path,'rb'))
        prev_doc_count = len(idf)
        prev_corpus_length = len(tf_idf)

    for f in file_names:

        file1 = open(f,'r') # never use 'rb' for textual data, it creates something like,  {b'line-inside-the-doc'}
        
        #create word_count dict for all docs
        for line in file1:
            dict = {}
            #find the amount of doc a word is in
            for i in set(line.split()):
                if i in idf: idf[i] +=1
                else: idf[i] =1
            for word in line.split():
                #find the count of all words in every doc
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
            tf_idf.append(dict)
        file1.close()

    #calculating final TF-IDF values  for all words in all docs(line in a doc in this case)
    for doc in tf_idf:
        for key in doc:
            true_idf = math.log(len(tf_idf)/idf[key])
            true_tf = doc[key]/len(doc)
            doc[key] = true_tf * true_idf

    print(TAG,'Total number of unique words in corpus',len(idf),'( '+paint('++'+str(len(idf)-prev_doc_count),'g')+' )' if prev_file_path else '')
    print(TAG,'Total number of docs in corpus:',len(tf_idf),'( '+paint('++'+str(len(tf_idf)-prev_corpus_length),'g')+' )' if prev_file_path else '')
    return idf,tf_idf

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--docs", required=True, help="path to folder containing document files")
    ap.add_argument("-f", "--file", help="path to previous tf-idf file")
    args = vars(ap.parse_args())


    doc_paths = glob.glob(args['docs']+'*')    
    print(TAG,'Fetched files: ',doc_paths) 
    
    idf,tf_idf = find_tf_idf(doc_paths,args['file'])
    
    #dump the generated TF-IDF in a file for further usage.
    out_path = 'loadout.tfidfpkl'
    pickle.dump((idf,tf_idf), open(out_path,'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    print(TAG,'TF-IDF generation process ended, pickle file  dumped @ ',out_path)
