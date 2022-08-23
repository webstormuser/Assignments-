#!/usr/bin/env python
# coding: utf-8

# # 1. Is the Python Standard Library included with PyInputPlus?
# Ans : no ,it is not a part of inbuilt library in python .we have to manually install it using pip install PyInputPlus command 

# # 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# 
# ANS :You can import the module with import pyinputplus as pyip so that you can enter a shorter name when calling the module’s functions.
# 
# PyInputPlus has functions for entering a variety of input, including strings, numbers, dates, yes/no, True/False, emails, and files. While input() always returns a string, these functions return the value in an appropriate data type. The inputChoice() function allow you to select one of several pre-selected options, while inputMenu() also adds numbers or letters for quick selection.

# # 3. How do you distinguish between inputInt() and inputFloat()?
# PyInputPlus is a Python module used for taking inputs with additional validation features. PyInputPlus will keep asking the user for text until they enter valid input.inputInt() : Accepts an integer value. This also takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  for bounds. Returns an int.
# inputFloat() : Accepts a floating-point numeric value. Also takes additional ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  parameters. Returns a float.

# # 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
# ANS :By using pyinputInt.inputInt(min=0,max=99) we can enter while number between 0 and 99

# In[69]:


#!pip install PyInputPlus


# In[78]:


import pyinputplus as pi
pi.inputInt(min=0,max=99)


# # 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# ANS :Ans: we can use allowRegexes and blockRegexes keyword arguments to take list of regular expression strings to determine what the pyinputplus function will reject or accept valid input.

# # 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# Ans: The statement inputStr(limit=3) will throw two exceptions ValidationException and RetryLimitException. The first exception is thrown because blank values are not allowed by inputStr() function by default. it we want to consider blank values as valid input, we have to set blank=True.

# In[85]:


import pyinputplus as pi
#pi.inputStr(limit=3)#throws an error
pi.inputStr(limit=3,blank=True) #control strop after 1st execution of blank


# # 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
# Ans: Since the default parameter is set to hello. after blank input is entered three times instead of raising RetryLimitException exception. the function will return hello as response to the calling function

# In[86]:


import pyinputplus as pi
pi.inputStr(limit=3,default='hello')


# In[ ]:




