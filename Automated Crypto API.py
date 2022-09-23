#!/usr/bin/env python
# coding: utf-8

# In[24]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Enter Your Crypto API Key',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  


# In[2]:


type(data)


# In[25]:


import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.json_normalize(data['data'])

df['timestamp'] = pd.Timestamp('now') #GMT+3 For Me

df


# In[51]:


def api_runner():
    global df3
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'20',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'Enter Your Crypto API Key',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.Timestamp('now') #GMT+3 For Me
    df3 = pd.concat([df,df2])
    
    if not os.path.isfile(r'D:\Data\CryptoAPI\API.csv'):
       df3.to_csv(r'D:\Data\CryptoAPI\API.csv', header = 'column_names') 
    else:
       df3.to_csv(r'D:\Data\CryptoAPI\API.csv', mode = 'a', header = False) 


# In[54]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Working')
    sleep(60)
exit()


# In[55]:


df3


# In[56]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[57]:


df3


# In[76]:


df4 = df3.groupby('name', sort = False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df4


# In[77]:


df5 = df4.stack()
df5


# In[78]:


type(df5)


# In[79]:


df6 = df5.to_frame(name = 'values')
df6


# In[80]:


type(df6)


# In[81]:


df6 = df6.reset_index()


# In[82]:


df6


# In[83]:


df6 = df6.rename(columns = {'level_1' : 'percent_change'})
df6


# In[84]:


df6['percent_change'] = df6['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'],['1h', '24h', '7d', '30d', '60d', '90d'])
df6


# In[70]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[85]:


sns.catplot(x = 'percent_change', y = 'values', hue = 'name', data = df6, kind = 'point')


# In[88]:


df7 = df3[['name', 'quote.USD.price', 'timestamp']]
df7 = df7.query('name == "Bitcoin"')
df7


# In[ ]:




