#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dict1= {
    "name": ["harry","Krishna","Uday"] ,
    "marks":[90,34,89],
    "city":["jaipur","chandigarh","Mumbai"]
}


# In[3]:


df = pd.DataFrame(dict1)


# In[4]:


df


# In[5]:


df.to_csv("marks.csv")


# In[6]:


df.to_csv("marks.csv", index=False)


# In[7]:


df.head(2)


# In[8]:


df.tail(2)


# In[9]:


df.describe() # show different operations results on columns with integers


# In[10]:


train = pd.read_csv('train.csv')


# In[11]:


train


# In[12]:


train['speed']


# In[13]:


train['speed'][2]


# In[14]:


train['speed'][2] = 110


# In[15]:


train


# In[16]:


train.to_csv("train.csv")


# In[17]:


train.index = ["1st","2nd","3rd","4th"]


# In[18]:


train


# In[19]:


ser = pd.Series(np.random.rand(20))


# In[20]:


ser


# In[21]:


type(ser)


# In[22]:


newdf = pd.DataFrame(np.random.randn(500,4) , index = np.arange(500)) #.rand or.randn


# In[23]:


newdf.head()


# In[24]:


newdf.tail(20)


# In[25]:


type(newdf)


# In[26]:


newdf.dtypes


# In[27]:


newdf[0][0] = "Krishna"


# In[28]:


newdf.dtypes


# In[29]:


newdf


# In[30]:


newdf.index


# In[31]:


newdf.columns




# In[32]:


newdf.to_numpy()


# In[33]:


newdf[0][0] = 93094


# In[34]:


newdf.T #transpose of matrix


# In[35]:


newdf.sort_index(axis = 1 , ascending = False) #axis  = 0 (row) , axis = 1 (columns)


# In[36]:


newdf2 = newdf #it will generated the mirror image of the newdf and the changes in newdf2 will lead tp change newdf to 


# In[37]:


newdf2 = newdf.copy()  #this will generate the copy of newdf


# In[38]:


newdf2[0][0] = "Krishna"


# In[39]:


newdf


# In[40]:


newdf2


# In[41]:


newdf.loc[0,0] = "Krishna" #this is the correct method to allocate the values in array not newdef[0][0]


# In[42]:


newdf


# In[43]:


newdf.columns = [0 , 1 , 2, 3]


# In[44]:


newdf


# In[45]:


newdf = newdf.drop(3 , axis =1)


# In[46]:


newdf


# In[47]:


newdf.loc[[1,4] , [1,2]] #it will return us the respective table


# In[48]:


newdf.loc[: ,[0,2]]


# In[49]:


newdf.loc[0,0] = 0.1


# In[50]:


newdf


# In[51]:


newdf.loc[(newdf[0]>1)  &  (newdf[2]<-0.5)] #like a query for table , return the table respective to condition


# In[52]:


newdf.iloc[0,2] # this iloc function is used when u can fetch table by index number but not index name 


# In[53]:


newdf.drop([0,3,4] , inplace =True) #inplace is used to make changes in original dataframe


# In[54]:


newdf


# In[55]:


newdf.reset_index(drop = True , inplace =True) # to reset the index numbe 


# In[56]:


newdf[1].isnull()


# In[57]:


intdf = pd.DataFrame([123, 234 ,345] ,
        [123, 234 ,345])


# In[58]:


intdf


# In[59]:


newdf


# In[60]:


newdf.columns = list('ABC')


# In[61]:


newdf.iloc[3 , 2]


# In[ ]:




