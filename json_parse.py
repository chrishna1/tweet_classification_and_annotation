import json
import pandas as pd
import csv #for writing into csv file

#open tweet.json
file = open('tweet.json')
json_data = json.load(file)
#close file
file.close()
#file closed.
    
#Now work with json_data

# Open/Create a file to append data
csvFile = open('tweet_df.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

df = pd.read_csv(file)
    for serialNo,tweet in enumerate(json_data):
        csvWriter.writerow(serialNo,tweet['id'],tweet['text'])
    
#reading csv
tweets = pd.read_csv('tweet_df.csv')
print(tweets.head(5))
