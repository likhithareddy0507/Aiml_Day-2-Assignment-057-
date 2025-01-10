#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


dir(np)


# In[5]:


x=np.array([40,67,57,90])
print(x)
print(type(x))


# In[12]:


a1 = np.array([[3,4,5,8],[7,2,8,np.NAN]])
print(a1)
print(a1.shape)
print(a1.dtype)


# In[16]:


# use of astype() to convert the data type
a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[18]:


# Mathematical operations on rows and cols
a2 = np.array([[3,4,5],[5,6,7],[9,3,2]])
a2


# In[20]:


print(a2.sum(axis = 1))
print(a2.sum(axis=0))


# In[22]:


# find mean value of rows and column
print(a2)
print(a2.mean(axis = 0))
print(a2.mean(axis = 1))


# In[24]:


# Matrix 
a2 = np.array([[2,4,5],[7,8,0],[1,5,4]])
a2


# In[26]:


a3 = np.array([[2,4,5],[7,8,0],[1,5,4]])
a3


# In[28]:


a3 = np.array([[2,4,5],[7,6,9],[1,8,3]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[30]:


a4 = np.array([[3,4,5],[7,3,2],[9,1,4],[10,9,8]])
a4


# In[ ]:




