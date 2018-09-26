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

with open('tweets.csv','w') as csvFile:
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    #write header
    csvWriter.writerow(['S.no', 'tweetid', 'tweettext']) #writerow accepts a list of values.

    df = pd.read_csv(file)
        for serialNo,tweet in enumerate(json_data):
            csvWriter.writerow([serialNo,tweet['id'],tweet['text']]) #writerow accepts a list of values.

            
#reading csv
tweets = pd.read_csv('tweets.csv')
print(tweets.head(5))
