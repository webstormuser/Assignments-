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


# # 1 What is difference between enclosing list comprehnsion in parenthesis and brackets ?

# ANS : The difference between enclosing list comprehnsion in parenthesis and brackets is that using () it acting as a generator and [] it represents the list

# In[15]:


g=[n*2 for n in range(10)]
l=(n*2 for n in range(10))
print(type(g))
print(type(l))
print(g)


# # 2. What is the relationship between generator and iterator?

# ANS : iterator is a object that uses next() method to get the next value of the sequence and generator is a function that produces or yields a sequence of values using a yield statement.

# In[30]:


li=['Welcome','to','iNeuron.ai']
l=iter(li) # getting iteration for list using iter()
while True:
    try:
        print(next(l))
    except StopIteration:
        break
print("Iteration come to an end")


# # 3.What are the signs that function is a generator function ?

# ANS :A function can be said to be generator function if and only if it contains yield statement inside it 

# In[36]:


#Regular function 
def negate_all(iterable):
    print("start")
    negatives=[]
    for i in iterable:
        print("negating",i)
        negatives.append(i)
    print("end")
    return negatives
    


# In[37]:


iterable=[2,3,4,5,6,7,8]
negate_all(iterable)


# In[46]:


#generator function 
def negate_all(iterable):
    print("start")
    for i in iterable:
        print("negating",i)
        yield -i
    print("end")
    


# In[47]:


iterable=[2,3,4,5,6,7,8]
negate_all(iterable)


# In[48]:


itera=iter(negate_all(iterable))
while True:
    try:
        print(next(itera))
    except StopIteration:
        break


# # 4 .What is the purpose of yield statement ?

# yield statement is used to generate a range or series of sequences to pass to iter function in generator 

# # 5.What is relationship between map calls( ) and list comprehnsion ? Make comparison and contrast between the two ?

# ANS : suppose we have a fuction and we want to compute this for diff values in single line of code there map() is used .
#     List comprehnsion is substitute for lambda function,map(),filter(),reduce().it follows the for m of mathematical set builder notation.
#     list comprenhsion is more conside and easier to read than map()
#     list comprenhsion allows to filter while map does not allow
#     list comprenhsion is faster than map()
#     map () is faster in case of calling alredy defined functions(no lambda function)

# In[49]:


#MAP FUNCTION 
def square(num):
    return num*num


# In[53]:


li=[1,2,3,4,5,6,7,8,9]
X=map(square,li)
print(X)
print(list(X)) 


# In[58]:


#LIST COMPRENHSION
li=[n*n for n in range(1,10)]
print(li)
li2=[n*n for n in range(1,10) if n%2==0] #list comprenhsion using condition inside it 
print(li2)


# In[ ]:




