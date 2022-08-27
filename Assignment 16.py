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


# # 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. 
# 
# For example, if you were born in 1980. the list would be years_list =
# [1980, 1981, 1982, 1983, 1984, 1985].

# In[39]:


def birth_list():
    year_list=[]
    byear=int(input("Enter year of your birth date"))
    logging.info(f' Birth year is :{byear}')
    for i in range(byear,byear+5):
        year_list.append(i)
    return year_list
    logging.info(year_list)


# In[40]:


birth_list()


# # 2. In which year in years_list was your third birthday?
# Remember, you were 0 years of age for your
# first year.

# In[41]:


def Bthday3_list():
    year_list=[]
    byear=int(input("Enter year of your birth date"))
    logging.info(f' Birth year is :{byear}')
    for i in range(byear,byear+5):
        year_list.append(i)
    logging.info(year_list)
    logging.info(f'3rd birthday is in :{year_list[3]}')
Bthday3_list()


# # 3.In the years list, which year were you the oldest?

# In[45]:


def oldest_list():
    year_list=[]
    byear=int(input("Enter year of your birth date"))
    logging.info(f' Birth year is :{byear}')
    for i in range(byear,byear+5):
        year_list.append(i)
    logging.info(f' The year iin which oldest is {year_list[-1]}')
oldest_list()


# # 4. Make a list called things with these three strings as elements: 
# 
# &quot;mozzarella&quot;, &quot;cinderella&quot;,
# &quot;salmonella&quot;.

# # 5. Capitalize the element in things that refers to a person and then print the list.
# 
# Did it change the
# element in the list?

# In[52]:


def cap_list():
    things=["mozzarella", "cinderella", "salmonella"]
    for ele in range(len(things)):
        if things[ele]=='cinderella':
            things[ele]=things[ele].capitalize()
    logging.info(things)
    
cap_list()


# # 6. Make a surprise list with the elements &quot;Groucho,&quot; &quot;Chico,&quot; and &quot;Harpo.&quot;
# 
# 

# # 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[86]:


surprise=["Groucho","Chico","Harpo"]
logging.info(f'Original list is :{surprise}')


# In[64]:


surprise[-1]=surprise[-1].lower()
surprise


# In[65]:


logging.info(surprise)


# In[88]:


logging.info(surprise[-1].lower()[::-1].capitalize())


# # 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
# chien, cat is chat, and walrus is morse.

# In[89]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
logging.info(e2f)


# # 9. Write the French word for walrus in your three-word dictionary e2f.

# In[90]:


logging.info(e2f.get('walrus'))


# # 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[91]:


f2e = dict([ele[::-1] for ele in e2f.items()])
logging.info(f2e)


# # 11. Print the English version of the French word chien using f2e.

# In[92]:


logging.info(f2e.get('chien'))


# # 12. Make and print a set of English words from the keys in e2f.

# In[93]:


logging.info(list(e2f.keys()))


# # 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# In[97]:


life={
    "animals":{
        "cats":["Henri","Grumpy","Lucy"],
        "octopi":{},     
        "emus":{}        
    },
    "plants":{},
    "others":{}
}


# In[99]:


logging.info(life)


# # 14. Print the top-level keys of life.

# In[102]:


logging.info(f'top level keys are:{life.keys()}')


# # 15. Print the keys for life[&#39;animals&#39;].

# In[105]:


logging.info(life['animals'].keys())


# # 16. Print the values for life[&#39;animals&#39;][&#39;cats&#39;]

# In[110]:


logging.info(life['animals']['cats'])


# In[ ]:




