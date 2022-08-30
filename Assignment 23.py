#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import logging


# In[2]:


logging.basicConfig(filename="assignment.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %('
                                                                          'message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


# # 1. What is the result of the code, and why?
# 
# 
# &gt;&gt;&gt; def func(a, b=6, c=8):
# print(a, b, c)
# &gt;&gt;&gt; func(1, 2)

# In[4]:


def func(a,b=6,c=8):
    print(a,b,c)
func(1,2) 

#The output 1 2 8 is because we didnt assign value for a hence it take value from function parameter
#which is 1 similary for b the value 6 will be overwritten by 2 and bedeafult c will take valu which is been passed


# # 2. What is the result of this code, and why?
# 
# &gt;&gt;&gt; def func(a, b, c=5):
# print(a, b, c)

# In[6]:


def func(a,b,c=5):
    print(a,b,c)
func(1, c=3, b=2) 


# ANS : value passed to function 1: b=2 and c=5 but inside call the value value of c get replaced and hence instead of 5 value of c is 3

# # 3. How about this code: what is its result, and why?
#     
# &gt;&gt;&gt; def func(a, *pargs):
# print(a, pargs)
# &gt;&gt;&gt; func(1, 2, 3)

# In[9]:


def func(a,*args):
    print(a,args)
func(1,2,3)


# ANS : first variable a is considered as single variable and *args define many variables in single variable 
#     hence 2,3 will be considered as single input becasue of that it returns in form of tuple

# # 4. What does this code print, and why?
# 
# &gt;&gt;&gt; def func(a, **kargs):
# print(a, kargs)
# &gt;&gt;&gt; func(a=1, c=3, b=2)

# In[10]:


def func(a,**kargs):
    print(a,kargs)
func(a=1,c=3,b=2)


# # ANS :when we passe any variable as **variable inside function it is treated as a dictionary hence when function parameter a=1 is passed it is considered as single value and return 1 
# but when c=3 and b=2 passed considered as dictionry and returned in dictionary format 

# # 5. What gets printed by this, and explain?
# 
# &gt;&gt;&gt; def func(a, b, c=8, d=5): print(a, b, c, d)
# &gt;&gt;&gt; func(1, *(5, 6))

# In[18]:


def func(a,b,c=8,d=5):
    print(a,b,c,d)
func(1,*(5,6))


# # 6. what is the result of this, and explain?
# 
# &gt;&gt;&gt; def func(a, b, c): a = 2; b[0] = &#39;x&#39;; c[&#39;a&#39;] = &#39;y&#39;
# &gt;&gt;&gt; l=1; m=[1]; n={&#39;a&#39;:0}
# &gt;&gt;&gt; func(l, m, n)
# 
# &gt;&gt;&gt; l, m, n

# In[20]:


def func(a,b,c):
    a=2
    b[0]='X'
    c['a']='y'
l=1
m=[1]
n={'a':0}
func(l,m,n)
l,m,n


# In[ ]:




