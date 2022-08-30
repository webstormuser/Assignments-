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


# # 1. Add the current date to the text file today.txt as a string.

# In[9]:


from datetime  import date
today=str(date.today())
with open("today.txt" ,"w") as file:
    file.write(today)
    file.close()


# In[10]:


get_ipython().system('type today.txt')


# # 2. Read the text file today.txt into the string today_string

# In[12]:


with open("today.txt","r") as file:
    today_string=file.read()
    logging.info(today_string)


# # 3. Parse the date from today_string.

# In[21]:


#to parse date from string strptime() is used 
#Syntax: datetime.strptime(date_string,format)
from datetime import datetime
parsed_data = datetime.strptime(today_string, '%Y-%m-%d')
logging.info(f'parsed date is :{parsed_data}')


# # 4. List the files in your current directory

# In[34]:


#to list the files in current directory os module is used 
import os
#os.listdir('C:\\Users\\shree')
for folders,subfolders,files in os.walk(os.getcwd()):
    for file in files:
        if '.ipynb' in file:
            print(file)
        #print(file)


# # 5. Create a list of all of the files in your parent directory (minimum five files should be available).

# In[35]:


import os 
os.listdir()


# # 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit

# In[50]:


import multiprocessing
import datetime
import time
import random
def process_one():
    logging.info(f'Process one has started on: {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    logging.info(f' Process one has ended on :{datetime.datetime.now()}')
def process_two():
    logging.info(f'Process two has started on: {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    logging.info(f' Process two has ended on :{datetime.datetime.now()}')
def process_three():
    logging.info(f'Process three has started on: {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    logging.info(f' Process three has ended on :{datetime.datetime.now()}')
        
if __name__=="__main__":
    p1=multiprocessing.Process(target=process_one())
    p2=multiprocessing.Process(target=process_two())
    p3=multiprocessing.Process(target=process_three())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    


# # 7. Create a date object of your day of birth.

# In[61]:


import datetime
dob=datetime.datetime.strptime("12-09-1990","%d-%m-%Y")
logging.info(f"bthdate is :{dob}")


# # 8. What day of the week was your day of birth?

# In[75]:


from datetime import datetime
dob=datetime(1990,9,12)
logging.info(f'Day of week of my birthdate is {dob.strftime("%A")}')


# # 9. When will you be (or when were you) 10,000 days old?

# In[77]:


from datetime import datetime, timedelta
my_dob = datetime.strptime("12/09/1990",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date


# In[ ]:




