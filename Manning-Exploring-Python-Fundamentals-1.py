#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = ["one", "two", "three"]


# In[2]:


b = a


# In[3]:


a[1] = "two and a half"


# In[4]:


a


# In[5]:


b


# In[6]:


#a and b are two labels of a same object


# In[7]:


c = "string"


# In[8]:


d = c


# In[9]:


d


# In[10]:


c = "new string"


# In[11]:


d


# In[12]:


c


# In[13]:


#c and d are two different variables


# In[14]:


e = 12


# In[15]:


f = e


# In[16]:


f


# In[17]:


e = 13


# In[18]:


f


# In[19]:


#e and f are two different variables


# In[20]:


g = 14.5


# In[21]:


h = g


# In[22]:


h


# In[23]:


g = 15


# In[24]:


h


# In[25]:


#g and h are two different variables


# In[26]:


i = (14, "tuple", 16)


# In[27]:


i


# In[28]:


j = i


# In[29]:


i = (1, 2, 3)


# In[30]:


j


# In[31]:


i


# In[32]:


#i and j are two different variables


# In[33]:


k = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}


# In[34]:


k


# In[35]:


print(k)


# In[36]:


l = k


# In[37]:


l


# In[38]:


k = {
    'Montreal' : 'Expos',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}


# In[39]:


k


# In[40]:


l


# In[41]:


#k and l are two different variables


# In[42]:


m = [1, ["test", "something"], 12.3]


# In[43]:


n = m


# In[44]:


m[1] = "something else"


# In[45]:


m


# In[46]:


n


# In[47]:


#m and n are two labels of the same variable


# In[48]:


o = 135


# In[49]:


p = o


# In[50]:


o = 136


# In[51]:


p == o


# In[52]:


#p and o are two different variables


# In[ ]:




