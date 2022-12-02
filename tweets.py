import tweepy
from tweepy import OAuthHandler
import pandas as pd


class TwitterClient(object): 
    def __init__(self):

        # Access twitter Credentials 
        consumer_key = 'H2BC0VG4ryxSRSOWu55v5gLq7'
        consumer_secret = 'vbPsG2SyFW9V45OVN4Zd7T5Sb0BlEpQ0O5NOY6VOp8eEks6jZe'
        access_token = '4777206672-mKdpANklpEAmix8SWYxnZPbH4ix354cZ7P6tjjD'
        access_token_secret = '0GLH8vvuzwoePOvdeczyByWWExEXzBlDPfP7pjHlCWUJ8'
        
        # OAuthHandler  
        auth = OAuthHandler(consumer_key, consumer_secret) 
        # set access token and secret 
        auth.set_access_token(access_token, access_token_secret) 
        
        # create tweepy API 
        
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
            
    
    
   

    # Function of tweets fetch
    def get_tweets(self, query, maxTweets = 50): 
        tweets = [] 
        sinceId = None
        max_id = -1
        tweetCount = 0
        tweetsPerQry = 80
        
        while tweetCount < maxTweets:
            
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry)
                else:
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                else:
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
                    
            for tweet in new_tweets:
                parsed_tweet = {} 
                parsed_tweet['tweets'] = tweet.text 

                if tweet.retweet_count > 0: 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
                        
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id

            
        
        return pd.DataFrame(tweets)
