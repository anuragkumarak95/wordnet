from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import http.client
import urllib3
from colorama import Fore,Back,Style
import sys
import config as cf
import re

TAG = Fore.BLUE+'Twitter-Scrapper/'+Style.RESET_ALL

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        j = json.loads(data)
        if 'text' in j.keys():
            sentence = ''
            for word in j['text'].split():
                # for every word in text,whose length is larger than or equals 5 and is made of alphabets only, enter that word to sentence.
                if len(word) >=5 and re.search(r'^[a-zA-z]+$',word): sentence += ' '+word
            # if final length of sentence is atleast greater than 10, print such sentences.
            if len(sentence.split()) >5: 
                print(sentence)
        return True

    def on_error(self, status):
        pass

def main(filter_list):
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(cf.consumer_key, cf.consumer_secret)
    auth.set_access_token(cf.access_token, cf.access_token_secret)
    stream = Stream(auth, l)

    streamer(stream,filter_list)

#func to call streamer, and if any connction error occurs ignore it and call iself recursively.
def streamer(stream,filter_list):
    #This line filter Twitter Streams to capture data by the keywords passed in sys.argv
    try:
        stream.filter(languages=['en'],track=filter_list,stall_warnings=True)
    except :
        #print(Fore.RED+TAG,'got an error',Style.RESET_ALL)
        streamer(stream,filter_list)

if __name__=='__main__':
    l = sys.argv
    del l[0]
    if not l: raise Exception(TAG+'please provide a list of filter words for streaming.')
    #print(TAG,'### Tweets Filtered according to string: ',str(l))
    main(l)
