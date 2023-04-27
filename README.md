# Sentiment Analysis with Twitter-Roberta

This script uses the Hugging Face Transformers library to perform sentiment analysis on tweets using the Twitter-Roberta model. The script can analyze the sentiment of tweets from a static CSV file or from the Twitter API.


## Installation
The script requires the following Python packages to be installed:

Packages      |
------------- |
transformers
scipy
pandas
tweepy
configparser  | 


You can install these packages using pip:

```pip install transformers scipy pandas tweepy configparser```

## Config

```[twitter]
API_key = <your_API_key>
API_key_secret = <your_API_key_secret>
access_token = <your_access_token>
access_token_secret = <your_access_token_secret>
```


## Usage

### Method 1: Use Static CSV file data

The script can analyze tweets from a CSV file with a "tweets" column containing the tweet text. To use this method, follow these steps:

Place the CSV file in the same directory as the script.
Update the CSV file name and path in the script.
Run the script using a Python interpreter.
The script will analyze the first 5 tweets in the CSV file and output the sentiment for each tweet in a new "sentiment" column.

### Method 2: Use Twitter API to get any particular Username's tweets

The script can also analyze tweets from a specific user on Twitter using the Twitter API. To use this method, follow these steps:

Create a Twitter API account and get the necessary API keys and access tokens.
Create a config.ini file in the same directory as the script.
Add the API keys and access tokens to the config.ini file.
Update the screen_name parameter in the api.user_timeline function to the desired Twitter username.
Run the script using a Python interpreter.
The script will get the last 200 tweets from the specified user and output the sentiment for each tweet in a new "sentiment" column in a pandas dataframe.

## Results

Tweet | Sentiment
| :--- | ---: 
I love people who are polite and honest  | Positive
I will ruin your life If you dont marry me  | Negative
Trees are beutiful gift of GOD  | Positive

## Credits

The sentiment analysis is performed using the Twitter-Roberta model, which is part of the Hugging Face Transformers library. The Twitter API is accessed using the Tweepy library.


