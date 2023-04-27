from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import pandas as pd
import tweepy
import configparser

def get_sentiment(tweet):
    # preprocess tweet
    tweet_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    # load model and tokenizer
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    sentiment_dict = {labels[i]: scores[i] for i in range(len(labels))}
    max_key = None
    max_value = -1

    for key, value in sentiment_dict.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

if __name__ =='__main__':

    #Method 1: Use Static CSV file data

    df = pd.read_csv('Twitter_Data.csv')
    df = df.head(5)
    df['sentiment'] = df['tweets'].apply(get_sentiment)
    print(df)

    #Method 2: Use Twitter API to get any particular Username's tweets
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['twitter']['API_key']
    api_secret = config['twitter']['API_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    #Authentication
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    #get tweets from user
    tweets = api.user_timeline(screen_name='@realDonaldTrump', count=200, tweet_mode='extended')
    #make df
    dfTweetsFromAPI = pd.DataFrame([tweet.full_text for tweet in tweets], columns=['tweets'])
    df['sentiment'] = df['tweets'].apply(get_sentiment)