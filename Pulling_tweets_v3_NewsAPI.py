"""
Created on Fri Oct  2 16:01:40 2020
@author: Aayush
Problem: Retrieving tweets between two dates from NewsAPI.org
"""

'''Limit is there for unpaid accounts - 100 max articles, 500 requests per day, back in time upto 1 month'''

import requests

# Retrieving the NewsAPI keys
f = open("Required_keys_NewsAPI.txt", "r")
NewsAPI_keys = f.read().split('\n')
NewsAPI_keys = [l.split('=')[1].strip() for l in NewsAPI_keys]
f.close()

# Setting up the sources
relevant_sources = ['abc-news', 'abc-news-au', 'al-jazeera-english', 'australian-financial-review', 'bbc-news',
 'bloomberg', 'business-insider', 'cbc-news', 'cbs-news', 'cnn', 'crypto-coins-news', 'financial-post', 'fox-news', 
 'google-news', 'google-news-uk', 'independent', 'msnbc', 'nbc-news', 'newsweek', 'politico',
 'reddit-r-all', 'reuters', 'the-hill',  'the-huffington-post', 'the-times-of-india',
 'the-wall-street-journal', 'the-washington-post', 'the-washington-times', 'time', 'usa-today']

sources = requests.get('https://newsapi.org/v2/sources?language=en&apiKey=' + NewsAPI_keys[0]).json()
sources = [s['id'] for s in sources['sources'] if s['id'] in relevant_sources]

# Setting up the url for pulling the data
url = ('http://newsapi.org/v2/everything?'
       'q=Oil-prices&'
       'from=2020-09-30&to=2020-10-30&'
       'sortBy=popularity&'
       'language=en&'
       'pageSize=100&'
       'apiKey='+NewsAPI_keys[0])

response = requests.get(url).json()

'''Pulling from the sources'''
all_responses = []
for src in sources:
    url = ('http://newsapi.org/v2/everything?'
           'q=Oil-prices'
           '&sources='+src+'&'
           'from=2020-10-01&to=2020-10-30&'
           'sortBy=popularity&'
           'language=en&'
           'pageSize=100&'
           'apiKey='+NewsAPI_keys[0])
    
    response = requests.get(url).json()
    all_responses.append(response)
