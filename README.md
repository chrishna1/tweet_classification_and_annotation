**Approach :**


Step 1 :

Created a words.txt that contains line seperated words.
I've taken 20 words, namely: 
natural, language, processing, word, embedding, vector, glove, word2vec, distributional, similarity, nlp, machine, learning, artificial, intelligence, deep, learning, hidden, layer, window.

Step 2 :

Created a script naming `tweet_scrape.py` that creates a json file that contains tweets scraped from twitter.
For scraping I've used Twitter credentials, authenticated it then used Tweepy api to get tweet object.

Step 3 : 

Created a script naming `json_parse.py` that parses tweet-id and tweet-text from Tweet Object and stores it into a csv file named `tweets.csv`. 
