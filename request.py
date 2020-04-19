#!/usr/bin/env python
# coding: utf-8

# In[1]:

import requests

# In[2]:

r = requests.get('https://inverted-list-python.azurewebsites.net/api/HttpTriggerList?param=1,2,3,a,e')

# In[3]:

print("Lista invertida: " + r.text) 




