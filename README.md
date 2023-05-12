# Sentiment Analysis with Twitter-Roberta

This script uses the Hugging Face Transformers library to perform sentiment analysis on tweets using the Twitter-Roberta model. The script can analyze the sentiment of tweets from a static CSV file or from the Twitter API.

## Data Pipeline

1. Data source: The data source for this pipeline is two fold: Either, we have a static CSV file that contains pre-collected tweets or Second, we use the Twitter API to collect tweets in real-time from a specific user.

2. Data cleaning: Before we can analyze the tweets, we need to clean and preprocess them. This involves removing duplicate entries, handling missing values, and converting the text into a format suitable for analysis. In this code example, the get_sentiment() function preprocesses the tweets by replacing user mentions and URLs with generic placeholders.

3. Data extraction: Once the data is cleaned, we can extract the features we need for analysis. In this code example, we extract the sentiment of each tweet using a pre-trained model and tokenizer from the Hugging Face Transformers library.

4. Model execution: After the features are extracted, we can execute our model to make predictions. In this example, the sentiment analysis model predicts whether the tweet is positive, negative, or neutral.

5. Data visualization: Finally, we can visualize the results of our analysis. In this code example, the sentiment analysis results are added to a DataFrame and printed to the console. However, in a real-world application, we might use a dashboarding tool like Grafana to visualize the results in real-time.


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


