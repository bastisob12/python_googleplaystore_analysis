#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


data=pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\googleplaystore.csv')


# In[47]:


data


# # Display Top 5 Rows of The Dataset

# In[37]:


data.head(5)


# # Check the Last 3 Rows of The Dataset

# In[38]:


data.tail(5)


# # Find Shape of Our Dataset (Number of Rows & Number of Columns)

# In[43]:


data.shape


# # Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[44]:


data.info()


# # Get Overall Statistics About The Dataframe

# In[45]:


data.describe()


# # Total Number of App Titles Contain Astrology

# In[46]:


data.columns


# In[52]:


data[data['App'].str.contains('Astrology')]


# # Find Average App Rating

# In[56]:


data['Rating'].mean()


# # Find Total Number of Unique Category

# In[57]:


data.columns


# In[58]:


data['Category'].nunique()


# # Which Category Getting The Highest Average Rating?

# In[62]:


data.groupby('Category')[('Rating')].mean().sort_values(ascending=False)


# # Find Total Number of App having 5 Star Rating

# In[63]:


data.columns


# In[74]:


len(data[data['Rating']==5.0])


# # Find Average Value of Reviews

# In[75]:


data.columns


# In[82]:


data['Reviews'].dtype


# In[109]:


data['Reviews']==data['Reviews'].replace('3.0M',3.0)


# In[114]:


data['Reviews']=data['Reviews'].astype('float')


# # Find Total Number of Free and Paid Apps

# In[115]:


data.columns


# In[123]:


data['Type'].value_counts()


# # Which App Has Maximum Reviews?

# In[124]:


data.head(1)


# In[134]:


data[data['Reviews'].max()==data['Reviews']]


# # Display Top 5 Apps Having Highest Reviews

# In[136]:


data.columns


# In[149]:


index=data['Reviews'].sort_values(ascending=False).head().index


# In[151]:


data.iloc[index]['App']


# # Find Average Rating of Free and Paid Apps

# In[153]:


data.columns


# In[161]:


data.groupby('Type')['Rating'].mean()


# # Display Top  5 Apps Having Maximum Installs

# In[162]:


data.columns


# In[169]:


data['Installs'].dtype


# In[178]:


data['Installs_1'].astype(int)


# In[176]:


data['Installs_1']=data['Installs_1'].str.replace('+','')


# In[181]:


data[data['Installs']=='Free']


# In[182]:


data['Installs_1']=data['Installs_1'].str.replace('Free','0')


# In[187]:


data['Installs_1']=data['Installs_1'].astype('int')


# In[188]:


data['Installs_1'].dtype


# In[189]:


data.head(1)


# In[192]:


index=data['Installs_1'].sort_values(ascending=False).head().index


# In[193]:


data.iloc[index]['App']

