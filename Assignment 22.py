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


# 1. What is the result of the code, and explain?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# print(X)
# 
# &gt;&gt;&gt; func()
# 
# 2. What is the result of the code, and explain?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI!&#39;
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)
# 
# 3. What does this code print, and why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI&#39;
# print(X)
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)
# 
# 4. What output does this code produce? Why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# global X
# X = &#39;NI&#39;
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)
# 
# 5. What about this code—what’s the output, and why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI&#39;
# def nested():
# print(X)
# nested()
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; X
# 
# 6. How about this code: what is its output in Python 3, and explain?
# 
# &gt;&gt;&gt; def func():
# X = &#39;NI&#39;
# def nested():
# nonlocal X
# X = &#39;Spam&#39;
# nested()
# print(X)
# 
# &gt;&gt;&gt; func()

# # 1. What is the result of the code, and explain?
# 
# 
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# print(X)
# 
# &gt;&gt;&gt; func()

# In[78]:


X='iNeuron'
def func():
    print(X)
func()


# Ans:above function will print the 'iNeuron' string which is passed to X since X is a global variable it will be accessed in function code

# # 2. What is the result of the code, and explain?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI!&#39;
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)

# In[88]:


X='iNeuron'
def func():
    X='Nil'
func()
print(X)


# ANS : The result of code func() will print nothing since we didnt print and if we write print(func()) output will be None since X's global value will be replaced by local value None 
#     but when print(X) is executed global value will be used hence output iNeuron will be displayed 

# # 3. What does this code print, and why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI&#39;
# print(X)
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)

# In[89]:


X='iNeuron'
def func():
    X="NI"
    print(X)
func()
print(X)


# ANS :first output NI ,is because of its local scope .X is replaced by local variable X in function and NI will be displayed and print(X) bydeafult take global scope variable hence iNeuron string is displated 

# # 4. What output does this code produce? Why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# global X
# X = &#39;NI&#39;
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; print(X)

# In[90]:


X='iNeuron'
def func():
    global X
    X="NI"
func()
print(X)


# In the above program, we declared a global variable inside the function func().before that  x has no effect of the global keyword.
# 
# Before and after calling func(), the variable x takes the value of local variable i.e x = NI.
# This is because we have used global keyword in x to create global variable inside the func() function (local scope).

# # 5. What about this code—what’s the output, and why?
# 
# &gt;&gt;&gt; X = &#39;iNeuron&#39;
# &gt;&gt;&gt; def func():
# X = &#39;NI&#39;
# def nested():
# print(X)
# nested()
# 
# &gt;&gt;&gt; func()
# &gt;&gt;&gt; X

# In[91]:


X = 'iNeuron'
def func():
    X = 'NI'
    def nested():
        print(X)
    nested()
func()
X        


# ANS:The output of the code is NI. the reason for this output is if a function wants to access a variable, if its not available in its localscope. it looks for the variable in its global scope. similarly here also function nested looks for variable X in its global scope. hence the output of the code is NI

# # 6. How about this code: what is its output in Python 3, and explain?
# >>> def func():
# X = 'NI'
# def nested():
# nonlocal X
# X = 'Spam'
# nested()
# print(X)
# >>> func()

# In[92]:


def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)
func()


# ANS: The output of the code is Spam. nonlocal keyword in python is used to declare a variable as not local.Hence the statement X = "Spam" is modified in the global scope. hence the output of print(X) statement is Spam

# In[ ]:




