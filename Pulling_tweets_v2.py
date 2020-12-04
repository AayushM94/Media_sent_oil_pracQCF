# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:58:15 2020
@author: Aayush
Problem: Retrieving tweets between two dates
"""

import tweepy as tw
import datetime
import json
import pandas as pd
from copy import deepcopy

# Keys
f = open("Required_keys_twitter.txt", "r")
keys = f.read().split('\n')
keys = [l.split('=')[1].strip() for l in keys]
f.close()
API_key, API_secret_key, access_token, access_secret_token = tuple(keys)

auth = tw.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tw.API(auth, wait_on_rate_limit=True)

username = ['OilandEnergy', 'CrudeOilPrices', 'PlattsOil', 'BloombergNRG', 'WorldOil', 'OPECnews', 'OPECSecretariat', 'FPRI', 
            'ReutersCommods', 'ETCommodities', 'IEA', 'EIAgov', 'ftenergy', 'BNCommodities', 'OGJOnline', 'Rigzone', 'energyintel']
#username = ['IEA', 'EIAgov', 'ftenergy', 'BNCommodities', 'OGJOnline', 'Rigzone', 'energyintel']

startDate = datetime.datetime(2019, 9, 1, 0, 0, 0)
endDate =   datetime.datetime(2020, 11, 1, 0, 0, 0)

tweets = {}
for user in username:
    print('\nFetching tweets from handle -@', user,'\n', sep = '')
    usertweets = []
    tmpTweets = api.user_timeline(user, count = 200, exclude_replies = True)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            json_str = json.dumps(tweet._json)
            parsed = json.loads(json_str) 
            usertweets.append(parsed)
    
    try:
        while (tmpTweets[-1].created_at > startDate):
            print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
            tmpTweets = api.user_timeline(user, max_id = tmpTweets[-1].id, exclude_replies = True)
            for tweet in tmpTweets:
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    json_str = json.dumps(tweet._json)
                    parsed = json.loads(json_str) 
                    usertweets.append(parsed)
    except IndexError:
        tweets[user] = usertweets
        continue
    
    tweets[user] = usertweets


tweets_v1 = deepcopy(tweets)
tweets_df = pd.DataFrame()
for user in list(tweets_v1.keys()):
    if len(tweets_v1[user])==0:
        del tweets_v1[user]
        continue
    usertweets_df = pd.DataFrame(tweets_v1[user])
    usertweets_df['Tw_handle'] = user
    usertweets_df = usertweets_df[['Tw_handle', 'created_at', 'text']]
    tweets_df = pd.concat([tweets_df, usertweets_df])
tweets_df.reset_index(drop=True, inplace = True)

tweets_df_old = pd.read_csv('fetched_tweets_v2.csv')
tweets_df_old = pd.concat([tweets_df_old, tweets_df])
tweets_df_old.to_csv('fetched_tweets_v2.csv', index = False)

