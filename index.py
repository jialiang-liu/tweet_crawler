import tweepy
import sys
import json
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()


with open("final.json",'r') as f:
    for line in f:
        json_data = json.loads(line)
        if json_data['place'] is not None:
            print(json_data['place']['bounding_box']['coordinates'][0][1])
            twitter = {"userName" :json_data['user']['name'],
                "time": json_data['created_at'],
                "text" : json_data['text'],
                #"location" : json_data['place']['bounding_box']['coordinates'][0],
                "url" : json_data['entities']['urls'],
                "location" : json_data['place']['bounding_box']['coordinates'][0][1]
                }
        
            es.index(index = "idx_twp", body = twitter, doc_type = "twitter_twp")


                                      
