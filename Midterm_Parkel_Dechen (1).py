#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Convert txt file into a readable list in Python while importing all necessary libraries.
import re
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np


numdata=open("C:/Users/deche/OneDrive - The George Washington University/Freshman Year/Spring 2023/Intro to Computing/Mid-term Project (1)/Mid-term Project/numbers.txt", "r")
numstring=numdata.read()
numlist=re.split(r',|\n', numstring)
print(numlist)


# In[2]:


#Converted list into a dictionary so i could count frequency
d = {}
for item in numlist:
    if item not in d.keys():
        d[item]=1
    else:
        d[item]+=1
d


# In[3]:


#Here I uploaded the file to foler as a json file
path = r"C:/Users/deche/OneDrive - The George Washington University/Freshman Year/Spring 2023/Intro to Computing/Mid-term Project (1)/Mid-term Project/out.json"
with open(path, "w") as out:
    json.dump(d,out)
f=open("C:/Users/deche/OneDrive - The George Washington University/Freshman Year/Spring 2023/Intro to Computing/Mid-term Project (1)/Mid-term Project/out.json","r")
f


# In[13]:


df=pd.read_csv("C:/Users/deche/OneDrive - The George Washington University/Freshman Year/Spring 2023/Intro to Computing/Mid-term Project (1)/Mid-term Project/The Good Stuff Stats - Sheet13.csv")
df


# In[14]:


plt.pie(df["Times Listened"], labels=df["Song Title"])
plt.show()

