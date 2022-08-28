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


# # 1. Assign the value 7 to the variable guess_me. Then,
# write the conditional tests (if, else, and elif) to
# print the string &#39;too low&#39; if guess_me is less than 7, &#39;too high&#39; if greater than 7, and &#39;just right&#39; if equal
# to 7.

# In[8]:


def guess_me_value(guess_me):
    if guess_me < 7 :
        logging.info("too low")
    elif guess_me > 7:
        logging.info("too high")
    elif guess_me ==7:
        logging.info("just right")
guess_me=7
guess_me_value(guess_me)
guess_me=6
guess_me_value(guess_me)
guess_me=15
guess_me_value(guess_me)


# # 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. 
# Write a while
# loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
# guess_me, print &#39;found it!&#39; and exit the loop. If start is greater than guess_me, print &#39;oops&#39; and exit
# the loop. Increment start at the end of the loop.

# In[10]:


guess_me=7
start=1
while True:
    if start<guess_me:
        logging.info("too low")
    elif start ==guess_me:
        logging.info("found it")
        break
    else:
        logging.info("oops")
        break
    start=start+1    


# # 3. Print the following values of the list [3, 2, 1, 0] using a for loop.

# In[15]:


l=[]
for i in range(4):
    num=int(input("Enter number into list"))
    l.append(num)
logging.info(l)


# # 4. Use a list comprehension to make a list of the even numbers in range(10)

# In[17]:


#First approach
even=[]
even1=[]
for i in range(0,10+1,2):
    even.append(i)
logging.info(f'By first approach {even}')
for i in range(0,10+1):
    if (i%2==0):
        even1.append(i)
logging.info(f'By second approach {even1}')


# # 5. Use a dictionary comprehension to create the dictionary squares. 
# Use range(10) to return the
# keys, and use the square of each key as its value.

# In[18]:


# Method 1
logging.info(dict([(x,pow(x,2)) for x in range(10)]))
# Method 2
logging.info({x:x**2 for x in range(10)})


# # 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

# In[23]:


logging.info({x for x in range(10) if (x%2!=0)})


# # 7. Use a generator comprehension to return the string &#39;Got &#39; and a number for the numbers in range(10). Iterate through this by using a for loop.

# In[78]:


gen=('Got_'+str(i) for i in range(10))
gen_list=[]
for i in gen:
    gen_list.append(i)
logging.info(gen_list)


# # 8. Define a function called good that returns the list [&#39;Harry&#39;, &#39;Ron&#39;, &#39;Hermione&#39;].

# In[80]:


def good():
    X=["Harry","Ron","Hermione"]
    return X
print(good())


# # 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
# for loop to find and print the third value returned.

# In[81]:


def get_odds():
    output=[]
    for i in range(10):
        if i%2==1:
            output.append(i)
    yield output


# In[82]:


get_odds()


# In[86]:


next(get_odds())


# In[87]:


next(get_odds())[2]


# # 10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print &#39;Caught an oops&#39;.

# In[93]:


class OopsException(Exception):
    pass
    
    def number(input):
        if number <0 :
            raise OopsException(n)
    def text(words):
        if words !=str:
            raise OopsException(t)
try :
    number(-8)
except Exception as e :
    print("Caught an oops-->",e)
try:
    text(123)
except Exception as e :
    print("Cought an oops--->",e)


# # 11. Use zip() to make a dictionary called movies that pairs these lists: titles = [&#39;Creature of Habit&#39;, &#39;Crewel Fate&#39;] and plots = [&#39;A nun turns into a monster&#39;, &#39;A haunted yarn shop&#39;].

# In[104]:


movies={
    "title":['Creature of Habit', 'Crewel Fate'],
    "plots": ['A nun turns into a monster', 'A haunted yarn shop']
}
logging.info(movies)


# In[105]:


title=['Creature of Habit', 'Crewel Fate']
plots=['A nun turns into a monster', 'A haunted yarn shop']
movies=dict(zip(title,plots))
logging.info(movies)


# In[ ]:




