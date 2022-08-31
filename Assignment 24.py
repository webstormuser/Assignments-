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


# # 1. What is the relationship between def statements and lambda expressions ?

# In[7]:


def squre(num):
    print(f"Sqaure of {num} is {num*num}")
squre(5)
x=lambda a:a*a
print(f'Sqaur is {x(5)}')


# # 2. What is the benefit of lambda?

# The lambda keyword in Python provides a shortcut for declaring small anonymous functions. Lambda functions behave just like regular functions declared with the def keyword. They can be used whenever function objects are required.

# # 3. Compare and contrast map, filter, and reduce.?

# The map(), filter() and reduce() functions bring a bit of functional programming to Python. All three of these are convenience functions that can be replaced with List Comprehensions or loops, but provide a more elegant and short-hand approach to some problems.
# 
# The map() Function
# The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
# 
# The syntax is:
# 
# map(function, iterable(s))
# 
# 
# The filter() Function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.
# 
# As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.
# 
# The syntax is:
# 
# filter(function, iterable(s))
# 
# 
# 
# The reduce() Function
# reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
# 
# Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
# 
# The syntax is:
# 
# reduce(function, sequence[, initial])

# In[22]:


#map ()
def list_of_fruits(s):
    return s[0]=="A"
        
        
fruits=["Banana","Apple","Apricote","Orange","Papaya"]
map_obj=map(list_of_fruits,fruits)
print(list(map_obj))

result_list = list(map(lambda s: s[0] == "A", fruits))#using lambda function
print(result_list)


# In[24]:


#filter()
#map ()
def list_of_fruits(s):
    return s[0]=="A"
        
        
fruits=["Banana","Apple","Apricote","Orange","Papaya"]
map_obj=filter(list_of_fruits,fruits)
print(list(map_obj))

result_list = list(filter(lambda s: s[0] == "A", fruits))#using lambda function
print(result_list)


# In[30]:


#reduce() it works differently as map () and filter () it returns single value instead of list
from functools import reduce
X=[1,2,3,4]
print(f'Initial values addition :{reduce(lambda x,y:x+y,X)}')
print(f'After addition  values addition :{reduce(lambda x,y:x+y,X,10)}')


# # 4. What are function annotations, and how are they used?

# Function annotations are completely optional both for parameters and return value.
# 
# Function annotations provide a way of associating various parts of a function with arbitrary python expressions at compile time.
# 
# The PEP-3107 makes no attempt to introduce any kind of standard semantics, even for the built-in types. All this work left to the third-party libraries.
# 
# 
# 
# 

# In[34]:


def func(x:'annotating x', y: 'annotating y', z: int) -> float: 
       print(x + y + z)
func(2,3,-4)


# In[36]:


func('Function','-','Annotation')


# # 5. What are recursive functions, and how are they used?

# # What are recursive functions used for?
# Image result for What are recursive functions, and how are they used?
# Recursion is a technique used to solve computer problems by creating a function that calls itself until your program achieves the desired result.
# A recursive function is a function defined in terms of itself via self-referential expressions. This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result.

# In[43]:


def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# # 6. What are some general design guidelines for coding functions?

# Safe: It can be used without causing harm.
# Secure: It can't be hacked.
# Reliable: It functions as it should, every time.
# Testable: It can be tested at the code level.
# Maintainable: It can be maintained, even as your codebase grows.
# Portable: It works the same in every environment.

# # 7. Name three or more ways that functions can communicate results to a caller.

# A Function in Python is a piece of code which runs when it is referenced. It is used to utilize the code in more than one place in a program. It is also called method or procedure. Python provides many inbuilt functions like print(), input(), compile(), exec(), etc. but it also gives freedom to create your own functions.
# 

# In[ ]:




