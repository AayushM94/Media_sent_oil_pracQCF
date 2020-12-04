"""
Created on Sun Nov  1 14:53:46 2020
@author: Aayush
Problem: Retrieving tweets between two dates from NewsAPI.org
"""

import datanews
import datetime

# Retrieving the Datanews.io keys
f = open("Required_keys_DataNews.io.txt", "r")
NewsAPI_keys = f.read().split('\n')
NewsAPI_keys = [l.split('=')[1].strip() for l in NewsAPI_keys]
f.close()



# Pulling the results
#response = datanews.headlines(q='SpaceX', language=['en'])
#articles = response['hits']
#print(articles[0]['title'])

startDate = datetime.date(2020, 3, 1)
endDate =   datetime.date(2020, 9, 1)

# Setting up the url for pulling the data
url = ('http://api.datanews.io/v1/news?'
       'q=Oil-prices&'
       'from='+str(startDate)+'&to='+str(endDate)+'&'
       'language=en&'
       'apiKey='+NewsAPI_keys[0])

response = requests.get(url).json()
