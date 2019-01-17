#Import required library.

# !pip install tweepy
import json
import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = XXXXX
consumer_secret = XXXX
access_token = XXXX
access_token_secret = XXXXX

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#Authenticated.

#Open words.txt file
#and
#Open(or create if there isn't any) tweet.json file

with open('words.txt') as words, open('tweet.json','w+') as file:
  array_json = [] #list that stores json object
  for word in words:
    for i,tweet in enumerate(tweepy.Cursor(api.search,q=word,count=100,
                               lang="en").items()):
        array_json.append(tweet._json) # extend destroy the dict structure. so use append
        if i > 50:
          break
  json.dump(array_json,file,sort_keys = True,indent = 4) #dumping the list into json file.        

#Now we have a json file created.
