#!/usr/bin/env python
# coding: utf-8

# # Print First Hello World

# In[6]:


print("hello world")


# In[7]:


print("I'm going up")


# # Variables

# In[8]:


x= 3


# In[9]:


get_ipython().run_line_magic('whos', '')


# In[10]:


print(type(x))


# In[11]:


x = 5.7


# In[12]:


print(type(x))


# In[13]:


abcd = 556.3


# In[14]:


get_ipython().run_line_magic('whos', '')


# In[15]:


a, b, c, d = 3, -5, 2, 4.3


# In[16]:


get_ipython().run_line_magic('whos', '')


# In[17]:


del abcd


# In[18]:


get_ipython().run_line_magic('whos', '')


# In[20]:


c = 2+3j


# In[21]:


print(type(c))


# In[22]:


s = "This is my life"


# In[23]:


print(type(s))


# # Operators

# In[24]:


get_ipython().run_line_magic('whos', '')


# In[25]:


sumOfAandB = a + b


# In[26]:


print(sumOfAandB)


# In[27]:


print(type(sumOfAandB))


# In[29]:


type(a + d)


# In[30]:


e = (a+b)**d - a


# In[31]:


print(e)


# In[32]:


10 // 3


# In[33]:


10 / 3


# In[34]:


_


# In[35]:


3x = 23


# A variable name doesn't start with a digit
# How to define a variable name then?

# # Type Bool 

# In[37]:


a  = True
b = True
c = False


# In[38]:


get_ipython().run_line_magic('whos', '')


# In[39]:


print(a and b)
print (a and c)
print (c and a)


# In[40]:


d = a or c
print(d)


# In[41]:


not(d)


# In[42]:


not(b)


# In[43]:


(a and b) or (c or d) and (a and d)


# # Comparaisons

# In[44]:


print(2 < 3)


# In[45]:


x = 2 > 3


# In[47]:


print(type(c))


# In[48]:


d = (3 == 4)


# In[49]:


print(d)


# In[50]:


3==3.0


# In[51]:


x =4
y = 9
z = 5
r = -3


# In[53]:


(x <y) and (z<y) or(r == x)


# In[54]:


(x <y) and (r == x) or(z<y)


# In[55]:


True and False or True


# In[57]:


# And will be applied before Or


# In[58]:


print((not (2!=3) and True) or (False and True))


# # Useful Functions

# In[ ]:


# Round Fucntion


# In[59]:


print(round(5.64658))


# In[60]:


print(round(4.3))


# In[62]:


print(round(4.3646 , 3))


# In[63]:


# Divmod function returns quotient and the remainder in a tuple


# In[64]:


divmod(12,5)


# In[65]:


divmod(23, 6)


# In[66]:


# isinstance check the type of argument


# In[67]:


isinstance("carrot", int)


# In[68]:


isinstance(1.0, int)


# In[69]:


isinstance(12, int)


# In[70]:


isinstance(4 + 4j, complex)


# In[71]:


# pow(x, y, z) raises x to the power of y and remainder by z (x**y)%z


# In[72]:


pow(3, 2, 4)


# In[73]:


# input takes the imput from the user


# In[78]:


a = input("Please Enter a number: ")


# In[83]:


print(type(a))


# In[84]:


a = int(a)


# In[85]:


print(type(a))


# In[86]:


print(a)


# In[87]:


a = int(input("Please Enter a number: "))


# In[88]:


print(a -23)


# In[91]:


# documentation pow? for documentation


# In[92]:


# implementation pow ?? ffor implementation


# In[94]:


get_ipython().run_line_magic('pinfo2', 'pow')


# In[ ]:




