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


# In[110]:


get_ipython().system('type zoo.py')
#inside zoo.py
def Hours():
    print("open 9-5 daily")


# # 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[113]:


import zoo
zoo.Hours()


# # 3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[114]:


imprt zoo as z
z.Hours()


# # 4. Import the hours() function as info and call it.

# In[115]:


from zoo import Hours()
hours()


# # 5. Create a plain dictionary with the key-value pairs &#39;a&#39;: 1, &#39;b&#39;: 2, and &#39;c&#39;: 3, and print it out.

# In[117]:


dict1={
    "a":1,
    "b":2,
    "c":3
}
print(dict1)


# # 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the
# same order as plain?

# In[118]:


from collections import OrderedDict
fancy = OrderedDict(dict1)
print(f'plain_dict -> {dict1}')
print(f'fancy -> {fancy}')


# # 7. Make a default dictionary called dict_of_lists and pass it the argument list. 
# Make the list
# dict_of_lists[&#39;a&#39;] and append the value &#39;something for a&#39; to it in one assignment. Print
# dict_of_lists[&#39;a&#39;].

# In[119]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


# In[ ]:




