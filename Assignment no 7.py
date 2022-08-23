#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging


# In[2]:


import sys


# In[3]:


logging.basicConfig(filename="assignment.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %('
                                                                          'message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


# # 1. What is the name of the feature responsible for generating Regex objects?
# -->re.compile() is responsible for generating Regex objects

# In[4]:


import re


# In[8]:


x=re.compile('\v\r\nsome_random_pattern')
type(x)
print(x)


# # 2. Why do raw strings often appear in Regex objects?
# Ans: Regular expressions use the backslash character ('\') to indicate special forms (Metacharacters) or to allow special characters (special sequences) to be used without invoking their special meaning. This collides with Python’s usage of the same character for the same purpose in string literals. Hence, Raw strings are used (e.g. r"\n") so that backslashes do not have to be escaped.

# # 3. What is the return value of the search() method?
# re.search(pattern, string, flags=0)
# Scan through string looking for a match to the pattern, returning
# a Match object, or None if no match was found.

# In[15]:


import re
print(re.search("I","Welcome to iNeuraon.ai Technology",flags=re.IGNORECASE))
print(re.search("Data Science","Welcome to Data Analyst course",flags=re.IGNORECASE))


# # 4. From a Match item, how do you get the actual strings that match the pattern?
# 
# The group() method returns strings of the matched text.

# In[22]:


import re
match = re.search('ineuron','Ineuron Full Stack Data Science Program', flags=re.IGNORECASE)
print('Output:',match.group())


# # 5. In the regex which created from the r&#39;(\d\d\d)-(\d\d\d-\d\d\d\d)&#39;, what does group zero cover?
# Group 2? Group 1?
# 
# Group 0 is the entire matchr'(\d\d\d)-(\d\d\d-\d\d\d\d)', group 1 covers the first set of parentheses(\d\d\d), and group 2 covers the second set of parentheses(\d\d\d-\d\d\d\d).
# 

# In[28]:


import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('my phone number is 444-555-66666')
print(mo.groups()) #returns complete searched string in tuple form
print(mo.group()) #retuns string format 
print(mo.group(1)) #returns first matched group
print(mo.group(2)) # returns second matched group


# # 6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
# 
# -->Periods and parentheses can be escaped with a backslash: \., \(, and \).

# In[29]:


# Example Program
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group())


# # 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
# 
# ANS :If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.

# In[44]:


import re
pattern=re.compile('lower')
print(pattern)
sequence='there is a garden of flowers'
print(pattern.findall(sequence))
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.findall('my phone number is 444-555-66666')
print(mo)


# # 8. In standard expressions, what does the | character mean?
# ANS :The | character signifies matching "either, or" between two groups.

# # 9. In regular expressions, what does the ? character stand for?
# Ans: In regular Expressions, ? characters represents zero or one match of the preceeding group.

# In[45]:


# Example Program
import re
match_1 = re.search("Bat(wo)?man","Batman returns")
print(match_1)
match_2 = re.search("Bat(wo)?man","Batwoman returns")
print(match_2)


# # 10.In regular expressions, what is the difference between the + and * characters?
# Ans: In Regular Expressions, * Represents Zero ore more occurances of the preceeding group, whereas + represents one or more occurances of the preceeding group.

# In[48]:


import re
match_1 = re.search("Bat(wo)*man","Batman returns")
print(match_1)
match_2 = re.search("Bat(m)+man","Batman returns")
print(match_2)


# # 11. What is the difference between {4} and {4,5} in regular expression?
# Ans: {4} means that its preceeding group should repeat 4 times. where as {4,5} means that its preceeding group should repeat mininum 4 times and maximum 5 times inclusively

# In[59]:


import re
haRegex = re.compile(r'(Ha){3,4}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHa')
print(mo1.group())
print(mo2)


# # 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?
# Ans: \d, \w and \s are special sequences in regular expresssions in python:
# 
# \w – Matches a word character equivalent to [a-zA-Z0-9_]
# \d – Matches digit character equivalent to [0-9]
# \s – Matches whitespace character (space, tab, newline, etc.)

# # 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
# Ans: \D, \W and \S are special sequences in regular expresssions in python:
# 
# \W – Matches any non-alphanumeric character equivalent to [^a-zA-Z0-9_]
# \D – Matches any non-digit character, this is equivalent to the set class [^0-9]
# \S – Matches any non-whitespace character

# # 14. What is the difference between .*? and .*?
# Ans: .* is a Greedy mode, which returns the longest string that meets the condition. Whereas .*? is a non greedy mode which returns the shortest string that meets the condition

# # 15. What is the syntax for matching both numbers and lowercase letters with a character class?
# Ans: The Synatax is Either [a-z0-9] or [0-9a-z]
# 

# # 16. What is the procedure for making a normal expression in regax case insensitive?
# Ans: We can pass re.IGNORECASE as a flag to make a noraml expression case insensitive

# # 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
# Ans: Dot . character matches everything in input except newline character .. By passing re.DOTALL as a flag to re.compile(), you can make the dot character match all characters, including the newline character.
# 

# # 18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
# Ans: The Ouput will be 'X drummers, X pipers, five rings, X hen'

# In[60]:



import re
numReg = re.compile(r'\d+')
numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
'X drummers, X pipers, five rings, X hen'


# # 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# Ans: re.VERBOSE will allow to add whitespace and comments to string passed to re.compile().

# In[61]:


# Without Using VERBOSE
regex_email = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$', re.IGNORECASE)
 
# Using VERBOSE
regex_email = re.compile(r"""
                            ^([a-z0-9_\.-]+)              # local Part like username
                            @                             # single @ sign 
                            ([0-9a-z\.-]+)                # Domain name like google
                            \.                            # single Dot .
                            ([a-z]{2,6})$                 # Top level Domain  like com/in/org
                         """,re.VERBOSE | re.IGNORECASE)   


# # 20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
# '42','1,234', '6,368,745'but not the following: '12,34,567' (which has only two digits between the commas) '1234' (which lacks commas)

# In[63]:


import re
pattern = r'^\d{1,3}(,\d{3})*$'
pagex = re.compile(pattern)
for ele in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',ele, '->', pagex.search(ele))


# # 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# 
# but not the following:
# 
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)

# In[64]:


Ans: pattern = r'[A-Z]{1}[a-z]*\sWatanabe'


# In[65]:


import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
namex = re.compile(pattern)
for name in ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']:
    print('Output: ',name,'->',namex.search(name))


# # 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# 
# but not the following:
# 
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

# In[66]:


Ans: pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'


# In[67]:


import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
casex = re.compile(pattern,re.IGNORECASE)
for ele in ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.'
,'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']:
    print('Output: ',ele,'->',casex.search(ele))


# In[ ]:




