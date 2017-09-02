import datetime, os, math, argparse, pickle, glob
from colorama import Fore, Style
'''TO-DO
1. find a better way to dump tf-idf values, too much data being used for now using list of dict
2. try to find more efficient ways to compute and calculate TF-IDF values , loop reduction required.
3. (DONE)change this code to pick a path and create TF-IDF dump from content of all of those files, where every line behaves like a independent document.
4. iintroduce a progress rate or better yet progress bar to the output.
'''

TAG = Fore.BLUE+'TF-IDF-GENE/'+Style.RESET_ALL
def find_tf_idf(file_names=['test.txt']):
    tf_idf = [] # will hold a dict of word_count for every doc(line in a doc in this case)
    idf = {}
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
    return tf_idf

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--docs", required=True, help="path to folder containing document files")
    args = vars(ap.parse_args())

    doc_paths = glob.glob(args['docs']+'*')    
    print(TAG,'Fetched files: ',doc_paths) 
    
    tf_idf = find_tf_idf(doc_paths)
    
    #dump the generated TF-IDF in a file for further usage.
    out_path = 'loadout.tfidfpkl'
    pickle.dump(tf_idf, open(out_path,'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    print(TAG,'TF-IDF generation process ended, pickle file  dumped @ ',out_path)
