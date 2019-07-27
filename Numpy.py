#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


vector = np.array([3, 4, 17,65])


# In[4]:


print(vector)


# In[5]:


matrix = np.array([[2, 5, 15], [20, 50, 30], [39, 99, 45]])


# In[6]:


print(matrix)


# In[7]:


print(matrix.shape)


# In[11]:


world_alcohol = np.genfromtxt('world-alcohol.csv', delimiter=',')
print(type(world_alcohol))


# In[ ]:





# In[ ]:




