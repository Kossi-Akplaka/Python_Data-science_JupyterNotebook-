#!/usr/bin/env python
# coding: utf-8

# In[1]:


def printSuccess():
    print("i'm done")
    print("Send me another task")


# In[2]:


printSuccess()


# In[3]:


3 + 8


# In[4]:


printSuccess()


# # Documentation

# In[9]:


def printSuccess():
    """ Documentation describes what the function is doing"""
    print(" ... ")


# In[7]:


def printSuccess2():
    """
        This function printSuccess2 is doing nothing except printing a message.
        That message is "hello"
    """
    print ("Hello")


# In[11]:


printSuccess()
printSuccess2()


# In[12]:


get_ipython().run_line_magic('pinfo2', 'printSuccess2')


# In[13]:


get_ipython().run_line_magic('pinfo2', 'len')


# In[14]:


help(printSuccess2)


# # Input Argument

# In[15]:


def printMessage(msg):
    print(msg)


# In[16]:


printMessage("How are you?")


# In[24]:


def printMessage(msg):
    """
        The function prints the message of the user and returns  a message if the input is a string type or not 
    """
    if isinstance(msg, str):
        print(msg)
    else:
        print("Your input argument is not a string")


# In[25]:


printMessage("This is the message")


# In[26]:


printMessage(23)


# In[27]:


y = "Hello there"
printMessage(y)


# In[28]:


def myPower(x, y):
    """This function computes the power of x to the y
    """
    c = x**y
    print(c)


# In[29]:


myPower(2, 4)


# In[32]:


def checkArgs(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(a + b)
    else:
        print(" this is not the same type")
                    


# In[33]:


checkArgs(2, 3.4)


# In[34]:


checkArgs(2, 4, 6)


# In[36]:


# order of the input argument is really important


# In[38]:


def add(x, y):
    c = x+y


# In[44]:


def myAdd(a,b):
    c = a + b
    return c


# In[45]:


d = myAdd(2, 3)
print(d)


# In[46]:


varOutside = 3
def g():
    print(varOutside)


# In[47]:


g()


# In[48]:


def r():
    a = 2
    b = 3
    d = "something"
    return a, b, d


# In[49]:


x, y, z = r()
print(x, y, z)


# # Variable number of arguments

# In[51]:


#It will receive a list args
def myAddUniv(*args):
    s = 0
    for i in range(len(args)):
        s+= args[i]
    return s


# In[52]:


print(myAddUniv(2, 4, 5))


# In[58]:


# multiples number of arguments in order
def printAllVariablesAndValues(**args):
    for x in args:
        print("the variable names is: ", x, "and value is: ", args[x])


# In[60]:


printAllVariablesAndValues(a = 3, b = "BB", c = "AEDF")


# In[62]:


# default constructor
def add(sum = 0):
    print(sum)


# In[63]:


add(2)


# In[64]:


add()


# # Modules

# In[69]:


# This is to import the whole module
import sys
sys.path.append('Desktop')
import Module as mod


# In[71]:


mod.addAllNumeric(2, 4, 5)


# In[76]:


# import only one function from the module
import sys
sys.path.append('Desktop')
from Module import addAllNumeric


# In[77]:


addAllNumeric(2, 3, 4)


# # Practice Problem

# In[8]:


"""
Given a list of numbers, make another list that contains all the items 
in sorted list order for min to max and your result will be another list
"""
def findMin(L, startIndex):
    m = L[startIndex]
    idx = startIndex
    for i in range(startIndex, len(L)):
        x = L[i]
        if x < m:
            m = x
            idx = i
        i+=1
    return m, idx


# In[11]:


a, b = findMin([1, 4, 5, 3, 11, 6], 2)


# In[12]:


print(a, b)


# In[6]:


def swap(L, idx1, idx2):
    temp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = temp
    return L


# In[7]:


swap([2, 4, 5, 1], 0, 3)


# In[33]:


def CheckIfNotNumeric2(L):
    for x in L:
        if not(isinstance(x, (int, float))):
            return False
        return True


# In[34]:


import sys
sys.path.append('Desktop')
from Module import CheckIfNotNumeric
def sortList(L):
    if not(CheckIfNotNumeric2):
        print("List doesn't not countain numeric value")
        return
    c = 0
    for x in L:
        m, idx = findMin(L, c)
        L = swap(L, c, idx)
        c+=1
    return L
    


# In[35]:


L2 = sortList([-2, 3, 1, 0, 8])


# In[36]:


print(L2)


# In[30]:


get_ipython().run_line_magic('pinfo2', 'CheckIfNotNumeric')

