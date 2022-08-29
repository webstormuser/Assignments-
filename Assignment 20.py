#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys 
import logging 


# In[2]:


logging.basicConfig(filename="assignment.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %('
                                                                          'message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s','%m-%d-%Y %H:%M:%S')
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


# # 1. Set the variable test1 to the string &#39;This is a test of the emergency text system,&#39; and save test1 to afile named test.txt.

# In[3]:


#test in file test.txt is "This is a test of emergency text system"
test1 = 'This is a test of the emergency text system,'
logging.info(test1)
with open('test.txt','w') as file:
    file.write(test1)
    file.close()


# In[ ]:


get_ipython().system('type test.txt')


# # 2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

# In[4]:


with open('test.txt','r') as file:
    test2 = file.read()
    
logging.info(test2)   
logging.info(test1 == test2)


# # 3. Create a CSV file called books.csv by using these lines:
#     
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992

# In[5]:


import csv


# In[6]:


header=["Title","Author","Year"]
data=[["The Weirdstone of Brisingamen","Alan Garner",1960],["Perdido Street Station","China Miéville",2000],["Thud!","Terry Pratchett",2005],["The Spellman Files","Lisa Lutz",2007],["Small Gods","Terry Pratchett",1992]]
with open("books.csv","w",encoding="utf-8",newline='') as file1:
    writer=csv.writer(file1)
    #write header to csv
    writer.writerow(header)
    #write data to csv 
    writer.writerows(data)


# # 4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

# In[7]:


import sqlite3


# In[8]:


db=sqlite3.connect("books.db")
cursor=db.cursor()
cursor.execute("create table books(title text,author  text, year int )")
db.commit()
db.close()


# # 5. Read books.csv and insert its data into the books table.

# In[9]:


import sqlite3
import csv
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
with open("books.csv","r") as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute("INSERT INTO books VALUES (?,?,?)",(book['Title'],book['Author'],book['Year']))
conn.commit()
conn.close()


# # 6. Select and print the title column from the books table in alphabetical order.

# In[20]:


import sqlite3
conn=sqlite3.connect("books.db")
cursor=conn.cursor()
output=cursor.execute("select Title from books order by Title ASC")
logging.info("title in Ascending order are as follows ")
for out in output :
    logging.info(out[0])
conn.commit()
conn.close()


# # 7 From the books table, select and print all columns in the order of publication.

# In[22]:


import sqlite3
conn=sqlite3.connect("books.db")
cursor=conn.cursor()
output=cursor.execute("select * from books order by Year")
logging.info("Publication year  in Ascending order are as follows ")
for out in output :
       logging.info(out)
conn.commit()
conn.close()


# # 8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.

# In[23]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
conn


# # 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

# In[28]:


get_ipython().system(' python -m pip install redis')


# In[32]:


import redis
conn = redis.Redis()
conn.hset('test',{
    'count':1,
    'name':'Fester Bestertester'
})
conn.hgetall('test')


# In[33]:


conn.hset("test",{
    "count":1,
    "name":"Fester Bestertester"
})


# In[35]:


conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')


# In[ ]:




