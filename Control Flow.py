#!/usr/bin/env python
# coding: utf-8

# # IF STATEMENT

# In[4]:


a = int(input())
b = int(input())
if a> b :
    print (a)
    print("I'm still in the block of if")
print("I'm outside the if condition")


# In[6]:


a = int(input())
b = int(input())
if a> b:
    print(a)
if a < b:
    print (b)


# # IF... ELSE CONDITION

# In[10]:


a  = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)


# In[11]:


a  = int(input())
b = int(input())
if a>b:
    print(a)
    print("if part")
else:
    print(b)
    print("else part")


# # If- Elif-Else

# In[13]:


a = 1
b = 5
if a == b:
    print("Equal")
elif a< b:
    print("a is less than b")
else:
    print("a is greater than b")


# # Short Form
# 

# In[16]:


a = int(input("Enter a marks: "))
if a >= 85:
    print("A grade")
elif (a < 85) and (a >= 80):
    print(" B grade")
elif (a < 80) and (a >= 75):
    print("C grade")
elif (a < 75) and (a >= 70):
    print("D grade")
else:
    print( "Below Average")
    
    


# In[18]:


a =3
if (a>10):
    print( "Is larger than 10")
elif not(a>10):
    print("else part")


# # Nested if

# In[25]:


a = int(input())
if(a >10):
    print("greater than 10")
    if(a >20):
        print("Greater than 20")
        if(a >30):
            print("Greater than 30")
        else:
            print("less than 30")
    else:
        print("less than 20")


# In[28]:


"""
User will enter a floating point number and your task is to find the integer portion before the point
and check if that inger portion is an even number
"""

number = float(input("Enter a floating number"))
number  = int (number)
if(number%2 == 0):
    print(" The number entered is even")
else:
    print("the number entered is odd")


# In[27]:


int(23.45)


# In[32]:


number = int(float(input("Enter a number")))
print("even ")if number%2==0  else print("odd")


# # While loop

# In[34]:


n = int(input("Max interations: "))
i = 1
while(i< n):
    print(i**2)
    i+=1
print('done')

    


# In[35]:


# while(true) break out of the loop / continue goes back up to the loop


# In[38]:


i = 10
while True:
        if i%9 == 0:
            print("Something")
            break
        else:
            print(i)
            i += 1
print('done')
            
        


# # For loop

# In[50]:


# L is a list
L = []
for i in range(10,0,-1):
    print(i)
    L.append(i**2)


# In[41]:


print(L)


# In[51]:


S = { "apple", 4.9, 3}
for x in S:
    print(x)
    


# In[81]:


Dictionary = {"fruit" :"apple", "number" : 4}
for x in Dictionary:
    print(x, Dictionary[x])
    print(x)


# In[ ]:


"""
Given a list of numbers, make another list that contains all the items 
in sorted list order for min to max and your result will be another list
"""
# Minimum value
L = [11, 4, 3, 5, 9]
for j in range(len(L)):
    m  = List[j]
    idx = j
    counter = j
    for i in range(j, len(L)):
        if L[i]<m:
            m = list[i]
            idx = counter
        counter +=1


    temp = L[j]
    L[j] = m
    L[idx] = temp
    
print(L)

