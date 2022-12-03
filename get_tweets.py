import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "H2BC0VG4ryxSRSOWu55v5gLq7"
api_secret_key = "vbPsG2SyFW9V45OVN4Zd7T5Sb0BlEpQ0O5NOY6VOp8eEks6jZe"
access_token = "4777206672-mKdpANklpEAmix8SWYxnZPbH4ix354cZ7P6tjjD"
access_token_secret = "0GLH8vvuzwoePOvdeczyByWWExEXzBlDPfP7pjHlCWUJ8"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # total list to store tweets
    tweets_list = []
    # no of tweets
    count = 20
    try:
        for tweet in api.search_tweets(q=text_query, count=count):
            print(tweet.text)
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed,', str(e))
        time.sleep(3)
        
        
  

#Refrance: https://github.com/vamshidhar199/twitterapp

