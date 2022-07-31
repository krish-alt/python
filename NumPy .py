#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


array = np.array([1,2,38,4] , np.int8)  #numPy types reference


# In[3]:


array


# In[4]:


array.shape 


# In[5]:


array.dtype



# In[6]:


arr = np.array(([1,2,3,4] , [2,3,4,5] , [5,3,5,6])) #array casting from tuples


# In[7]:


arr
   


# In[8]:


arr.shape


# In[9]:


arr.size


# In[10]:


arr.dtype


# In[11]:


arrlist = np.array([[1,2,3,4],[5,3,6,3],[345,4.4,2,5]]) #casting from list


# In[12]:


arrlist.shape


# In[13]:


arrlist.size


# In[14]:


arrlist.dtype


# In[15]:


arrDict = np.array({"name":["Krishna" , "Goyal" , "Uday"],
                   "Marks":[2,3,4],
                   "age":[18,12,14]})


# In[16]:


arrDict


# In[17]:


zeroes = np.zeros((6,6))


# In[18]:


zeroes


# In[19]:


rng = np.arange(14)


# In[20]:


rng


# In[21]:


lspace = np.linspace(1,10,4)  #give an array of given number and in given range 


# In[22]:


lspace


# In[23]:


emp = np.empty((7,3)) #ARRAY of random values


# In[24]:


emp


# In[25]:


emp_like = np.empty_like(rng) #will generate the same size array but empty values


# In[26]:


emp_like


# In[27]:


ide =np.identity(5)  #generate an identity matrix


# In[28]:


ide


# In[29]:


rng = rng.reshape(2,7) #1D array to 2D


# In[30]:


rng


# In[31]:


rng = rng.ravel() #2D to 1D


# In[32]:


rng


# In[33]:


arr


# In[34]:


arr.sum(axis = 0)


# In[35]:


arr.sum(axis = 1)


# In[36]:


arr.T #transpose the matrix


# In[37]:


arr.flat


# In[38]:


for i in arr.flat :
    print(i)


# In[39]:


arr.ndim #number of dimensions (2D)


# In[40]:


arr.nbytes #number of bytes 


# In[41]:


arr.argmax()


# In[42]:


arr.argmin()


# In[43]:


arr.argsort() #give indeces in which the matrix would be sorted


# In[44]:


arr.sort()


# In[45]:


arr


# In[46]:


arr2 = arr.copy()


# In[47]:


arr2


# In[48]:


arr2[1] = [2,4,2,45]


# In[49]:


arr2


# In[50]:


arr2 + arr


# In[51]:


arr*arr2


# In[52]:


arr2*arr


# In[53]:


arr2 - arr


# In[54]:


arr


# In[55]:


np.sqrt(arr2)


# In[56]:


np.where(arr == 3)


# In[57]:


np.count_nonzero(arr)


# In[58]:


import sys


# In[59]:


pyarr = list(rng)


# In[60]:


pyarr


# In[61]:


sys.getsizeof(1) * len(pyarr)


# In[62]:


rn = np.array(rng)


# In[63]:


rn


# In[64]:


rn.itemsize * rn.size


# In[ ]:




