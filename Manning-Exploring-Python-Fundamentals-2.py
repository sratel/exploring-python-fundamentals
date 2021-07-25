#!/usr/bin/env python
# coding: utf-8

# In[89]:


a = ["one", "two", "three"]


# In[90]:


b = a


# In[91]:


a[1] = "two and a half"


# In[92]:


print(f"value of a: {a}, id = {id(a)}")
print(f"value of b: {b}, id = {id(b)}")


# In[93]:


#a and b are two labels of a same object


# In[94]:


c = "string"


# In[95]:


d = c


# In[96]:


c = "new string"


# In[97]:


print(f"value of c: {c}, id = {id(c)}")
print(f"value of d: {d}, id = {id(d)}")


# In[98]:


#c and d refer to different objects


# In[99]:


e = 12


# In[100]:


f = e


# In[101]:


e = 13


# In[102]:


print(f"value of e: {e}, id = {id(e)}")
print(f"value of f: {f}, id = {id(f)}")


# In[103]:


#e and f refer to different objects


# In[104]:


g = 14.5


# In[105]:


h = g


# In[106]:


g = 15


# In[107]:


print(f"value of g: {g}, id = {id(g)}")
print(f"value of h: {h}, id = {id(h)}")


# In[108]:


#g and h refer to different objects


# In[109]:


i = (14, "tuple", 16)


# In[110]:


j = i


# In[111]:


i = (1, 2, 3)


# In[112]:


print(f"value of i: {i}, id = {id(i)}")
print(f"value of j: {j}, id = {id(j)}")


# In[113]:


#i and j refer to different objects


# In[114]:


k = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}


# In[115]:


l = k


# In[116]:


k = {
    'Colorado' : 'Broncos',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}


# In[117]:


print(f"value of k: {k}, id = {id(k)}")
print(f"value of l: {l}, id = {id(l)}")


# In[118]:


#k and l refer to different objects


# In[119]:


m = [1, ["test", "something"], 12.3]


# In[120]:


n = m


# In[121]:


m[1] = "something else"


# In[122]:


print(f"value of m: {m}, id = {id(m)}")
print(f"value of n: {n}, id = {id(n)}")


# In[123]:


#m and n are two labels referring to the same object


# In[124]:


o = 135


# In[125]:


p = o


# In[126]:


o = 136


# In[127]:


print(f"value of p: {p}, id = {id(p)}")
print(f"value of o: {o}, id = {id(o)}")


# In[128]:


#p and o refer to different objects

