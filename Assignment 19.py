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


# # 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?

# In[3]:


class Thing:
    pass
logging.info(Thing)
example=Thing()
logging.info(example)


# # 2. Create a new class called Thing2 and add the value &#39;abc&#39; to the letters class attribute. Letters should be printed.

# In[4]:


class Thing2:
    letters="abc"
logging.info(Thing2.letters)


# # 3. Make yet another class called, of course, Thing3. This time, assign the value &#39;xyz&#39; to an instanc(object) attribute called letters. Print letters. Do you need to make an object from the class to dothis?

# In[8]:


class Thing3:
    def __init__(self):
        self.letters="xyz"
try:
    logging.info(Thing3.letters)
except Exception as e:
    logging.error(e)
    th=Thing3()
    logging.info(th.letters)


# # 4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values &#39;Hydrogen,&#39; &#39;H,&#39; and 1.

# In[14]:


class Elements:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
try:
    logging.info(Elements.name +Elements.symbol+Elements.number)
except Exception as e:
    logging.error(e)
e=Elements("Hydrogen","H",1)
logging.info(f'Element name :{e.name} Symbol :{e.symbol}  Number is {e.number}')


# # 5. Make a dictionary with these keys and values: &#39;name&#39;: &#39;Hydrogen&#39;, &#39;symbol&#39;: &#39;H&#39;, &#39;number&#39;: 1. Then, create an object called hydrogen from class Element using this dictionary.

# In[19]:


dict1={
    "name":"Hydrogen",
    "symbol":"H",
    "number":1
}
print(dict1)
# Method 1
hydrogen = Elements(*dict1.values())
logging.info(f'Using Method #1 ->{hydrogen.name} {hydrogen.symbol} {hydrogen.number}')

# Method 2
hydrogen = Elements(**dict1)
print(f'Using Method #2 -> {hydrogen.name} {hydrogen.symbol}  {hydrogen.number}')


# # 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

# In[22]:


class Elements:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def dump(self):
        logging.info(f'{self.name} {self.symbol } {self.number}')
        
hyderogen =Elements("Hydrogen","H",1)
hyderogen.dump()


# # 7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.

# In[29]:


class Elements:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def __str__(self):
        return f'{self.name} {self.symbol } {self.number}'
hydrogen=Elements("Hydrogen","H",1)
logging.info(hydrogen)


# # 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# In[31]:


class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_symbol(self):
        return self.__symbol
    
    @property
    def get_number(self):
        return self.__number
    
hydrogen = Element('Hydrogen','H',1)
logging.info(hydrogen.get_name)
logging.info(hydrogen.get_symbol)
logging.info(hydrogen.get_number)


# # 9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). Th should return &#39;berries&#39; (Bear), &#39;clover&#39; (Rabbit), or &#39;campers&#39; (Octothorpe). Create one object fromeach and print what it eats.

# In[34]:


class Bear:
    def __init__(self):
        pass
    def eats(self):
        logging.info(f" bear eats Berries")
class Rabbit:
    def __init__(self):
        pass
    def eats(self):
        logging.info(f" Rabbit eats clover")
class Octothorpe:
    def __init__(self):
        pass
    def eats(self):
        logging.info(f" Octothorpe eats campers")
b=Bear()
b.eats()
r=Rabbit()
r.eats()
o=Octothorpe()
o.eats()
    


# # 10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). Thisreturns &#39;disintegrate&#39; (Laser), &#39;crush&#39; (Claw), or &#39;ring&#39; (SmartPhone). Then, define the class Robot thathas one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

# In[35]:


class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        print(self.laser.does(),self.claw.does(),self.smartphone.does())
        
r2d2 = Robot()
r2d2.does()


# In[ ]:




