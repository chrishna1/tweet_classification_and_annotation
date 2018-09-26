#Import required library.

# !pip install tweepy
import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = 'IsxY71d4o6NG7d2ZeUCH6etxW'
consumer_secret = 'jqNTCKO5PgZPH7mYp40fO5A392o6XOYzQXKVHtqO10xrTvJibw'
access_token = '4789665606-JHGodJKTmbjHGSVlF5ZZzZAXmsSwQnbQrAjo6zj'
access_token_secret = 'Hknc2PV2coSdcUQk1mbAGB3N2tH3PJgVxTd8qLQd9juVw'

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#Authenticated.

#Open words.txt file
#and
#Open(or create if there isn't any) tweet.json file

with open('words.txt') as words, open('tweet.json','w+') as file:
  for word in words:
    for i,tweet in enumerate(tweepy.Cursor(api.search,q=word,count=100,
                               lang="en").items()):
#         csvWriter.writerow([tweet.created_at, tweet])#.text.encode('utf-8')])
        json.dump(tweet._json,file,sort_keys = True,indent = 4)
        if i > 50:
          break
          

#Now we have a json file created.
  
  >>> with open('/home/insol/Downloads/tweet.json', 'r') as infile:
...     data = infile.read()
...     new_data = data.replace("}{" , "},{")
...     json_data = json.loads('[{}]'.format(new_data))
... 
>>> json_data
