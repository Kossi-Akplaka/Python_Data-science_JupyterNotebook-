#!/usr/bin/env python
# coding: utf-8

# # String 

# In[1]:


s = "Python is the best language"
t  = " It is good for dts"


# In[2]:


type(s)


# In[3]:


print(s)


# In[4]:


v = s + t
print(v)


# In[5]:


v = s + " and" + t
print(v)


# In[8]:


a = 12
b = " The price of this book"
print(b+ " is " + str(a))


# In[10]:


a = """
    This is line 1
    this is line 2
    this is line 3
    """
print(a)


# In[12]:


print(""" The following option are available:
        -A: does nothing
        -B: does something
""")


# In[13]:


get_ipython().run_line_magic('pinfo2', 'str')


# In[20]:


#slicing
s  = "How are you?"
print(s[8:11])
print(s[-4:-1])


# In[31]:


print(s[1:12:2])
print(s[ : 11:2])
print(s[: 4:-1])
print(len(s))
print(s[11])


# In[39]:


# strip remove the spaces from the string from beginning and from end
print(s.strip())
print(s.lower())
print(s.upper())
print(s.replace('o', 'a'))
#


# In[42]:


type(s.split(' '))


# In[48]:


s.casefold()
get_ipython().run_line_magic('pinfo2', 's.count')


# In[54]:


# return true if the string is in there
print("a" in s)
# return false if the string is not in there
print("a" not in s)
# String comparaison( first element)
"db"<"bca"


# In[62]:


#Escape correctors
print("We are in the age of \"amazingness\"")
print("c:\\nesktop\drive")
# raw string so treat everything as it is


# # list

# In[155]:


# ordered
L = [1, 3, 5, 3, 5]
L[1]
sum(L)


# # tuples

# In[95]:


# ordered, unchangeable
T = (1, 3, "name", "orange")
T2 = ('a', 'b')
print(T + T2)
T2.count('a')


# # Set

# In[121]:


# unordered
S = {1, 3, 5, 8, 3, "name"}
'1'in S
S.update({1, 4, 5})
print(S)


# # Dictionaries

# In[83]:


D = {'fruit': 'orange', 'size': 'big', 'color': 'orange'}
get_ipython().run_line_magic('pinfo2', 'D.update')


# In[104]:


D['shape'] = 'round'
print(D)
get_ipython().run_line_magic('pinfo2', 'D.update')


# In[105]:


E = {'fruit': 'mango', 'size': 'medium', 'color': 'yellow', 'shape': 'round'}


# In[110]:


D.update(E)
print(E)
print(D)
type(D)


# In[125]:


S[2]


# In[126]:


D


# In[127]:


for x in D:
    print(x, D[x])


# In[129]:


D2 = {'A':L, 'B':S, 'C':T, 'D':D}


# In[133]:


'name' in D2['B']


# In[134]:


L2 = [x**2 for x in range(10)]


# In[135]:


L2


# In[136]:


S = {x**2 for x in range(1, 20, 2)}


# In[137]:


S


# In[9]:


"""Student record containning ID of each student and the marks list of every subject. 
   Wants to compute the average
"""
# Getting the data
def getDataFromTeacher():
    D = {}
    while True:
        studentId = input('Enter student ID: ')
        if studentId in D:
            print('Student Id is already there')
        else:
            marksList = input('Enter the marks by separing each with the comma: ')
            moreStudents = input("Enter yes/no for ading more students: ")
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == 'no':
            return D
    


# In[10]:


studentData = getDataFromTeacher()


# In[25]:


studentData
for x in studentData:
        L = studentData[x]
        sum(L)


# In[26]:


def averageMarks(D):
    averageDictionary={}
    for x in D:
        L = D[x]
        sum = 0
        for i in L:
            sum += int(i)
        averageDictionary[x] = sum / len(L)
    return averageDictionary
        
            


# In[27]:


avMarks = averageMarks(studentData)


# In[28]:


def printAverage(D):
    for x in D:
        print("The student " + str(x) + " has an average of " + str(D[x]))
    


# In[29]:


printAverage(avMarks)


# In[ ]:




