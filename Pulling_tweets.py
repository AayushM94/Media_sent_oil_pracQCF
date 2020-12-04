# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:28:43 2020
@author: Aayush
Problem: Pulling feeds from twitter based on #oilprices
"""

import tweepy as tw
import json

# Keys
API_key = 'zioaT2chm3XpSpudWv5LzyyzT'
API_secret_key = '7pmszEX0IJkTH0ius6okCZcQturRuvFVBYVGvrPNddITmGTWDy'
access_token = '1510367640-MrIHp7j7mspjIqXXjaUVSmIxhOix9w9z0MzMkxG'
access_secret_token = '7PbW2JqyMSsuZ4UhpAyTC3tL3JN0gUvm6N4ryOglzzYaH'

auth = tw.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#oilprices" +' -filter:retweets -filter:replies'
date_since = "2020-03-10"

msgs = []
dict_msg = []
for tweet in tw.Cursor(api.search, q = search_words, lang="en", since = date_since, rpp=100).items(10):
    msg = [tweet.text, tweet.source, tweet.source_url, tweet.created_at]
    json_str = json.dumps(tweet._json)
    parsed = json.loads(json_str)    
    msgs.append(msg)
    dict_msg.append(parsed)      

