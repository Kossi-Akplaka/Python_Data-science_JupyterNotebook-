#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[1]:


"""Numpy is like a list but works much faster
   Focus on numeric data
"""
import numpy as np


# In[10]:


a = np.array([x**2 for x in range(3)], dtype= 'i')


# In[8]:


b = np.array([2, 5, 6])


# In[13]:


a.dtype


# In[ ]:


# Numpy dimensions


# In[14]:


get_ipython().run_line_magic('pinfo2', 'a.ndim')


# In[15]:


a = np.array([[1,2,3],[3,4,1]])


# In[16]:


a.ndim


# In[17]:


a[0,2]


# In[18]:


a[0][2]


# In[23]:


b =np.array([[1,2,3],[3,4,1], [12,3,4,3]])


# In[25]:


print(b)


# In[26]:


# numpy shape number of 


# In[28]:


b.shape


# In[29]:


A = np.array([2])


# In[30]:


A.ndim


# In[31]:


B = np.array(3)


# In[32]:


B.ndim


# In[34]:


get_ipython().run_line_magic('pinfo2', 'b.size')


# In[38]:


np.arange(20)
np.arange(2,10, 3)


# In[40]:


print(range(10))


# In[42]:


A= np.random.permutation(np.arange(10))


# In[43]:


print(A)


# In[51]:


A = np.arange(np.random.lognormal(1))


# In[52]:


print(A)


# In[54]:


get_ipython().run_line_magic('pinfo2', 'np.reshape')


# In[55]:


A = np.random.rand(1000)


# In[57]:


C = np.random.rand(2,3)


# In[58]:


C


# In[59]:


C = np.random.rand(2,3, 4,1)


# In[60]:


C


# In[61]:


D = np.arange(100).reshape(4, 25)


# In[62]:


D


# In[63]:


np.zeros(10)


# In[64]:


# indexing and slicing in numnpy


# In[65]:


A = np.arange(100)
B = A[1:54]


# In[66]:


B[0] = 23


# In[67]:


A


# In[68]:


B =A[1:54].copy


# In[70]:


A[::-5]


# In[73]:


idx = np.argwhere(A ==1200)[0][0]


# In[72]:


idx


# In[1]:


import numpy as np


# In[2]:


np.arange(5)


# In[7]:


A = np.round(10* np.random.rand(4,5))


# In[8]:


A


# In[11]:


A[2,2]
A[1,]


# In[18]:


A[1:3,1:3]


# In[19]:


A.T


# In[20]:


#linear algebra libray
import numpy.linalg as la


# In[30]:


A.sort()


# In[31]:


A


# In[36]:


A[[x for x in range(0,4, 2)]]


# In[41]:


A[(A<8)]


# In[38]:


A = np.arange(100)


# In[39]:


B = A[[range(1,20,4)]]


# In[40]:


B


# In[43]:


# &, and array and single object
# /, or
# ~, not
# broadcasting
# horizontal concatenation np.hstack,  horizontal concatenation vstack, storting np.stack


# In[44]:


A = np.round(10* np.random.rand(4,5))


# In[45]:


A


# In[46]:


A+3


# In[47]:


A + np.arange(20).reshape(4,5)


# In[48]:


B = np.round(10* np.random.rand(4,5))


# In[52]:


C = np.hstack((A,B))


# In[53]:


C


# In[57]:


A = np.random.permutation(np.arange(20))


# In[58]:


A


# In[60]:


np.sort(A)


# In[62]:


A = np.array(["abc",'howareyou','u565'])


# In[65]:


b = np.random.rand(100000)
get_ipython().run_line_magic('timeit', 'sum(b)')
get_ipython().run_line_magic('timeit', 'np.sum(b)')


# In[68]:


def sum(G):
    sum = 0
    for x in G:
        x += sum
    return x


# In[70]:


get_ipython().run_line_magic('timeit', 'sum(b)')


# # Pandas for handling data, processing and prepare the data

# In[72]:


import pandas as pd


# In[73]:


# Series handles one dimension array with values and index
data = pd.Series([1,2,3,4], index = ['afi', 'abla', 'ama', 'cat'])


# In[74]:


data.values


# In[75]:


data.index


# In[76]:


data['afi']


# In[77]:


The final index is included
data['afi':'ama']


# In[82]:


grades_dic = {'A':4,'B':3.5,'C':3,'D':2.5}
grads = pd.Series(grades_dic)


# In[83]:


grads


# In[84]:


grades_marks = {'A':85,'B':80,'C':75,'D':65}
marks = pd.Series(grades_marks)


# In[86]:


marks


# In[87]:


grads


# In[88]:


D = pd.DataFrame({'Marks':marks,'Grades':grads})


# In[89]:


D


# In[90]:


D.values


# In[92]:


D.values[1,1]


# In[93]:


D['ScalesMarks'] = D['Marks']/90


# In[94]:


D


# In[97]:


G = D[D['Marks'] > 76]


# In[98]:


G


# In[100]:


# Handling Missing data 


# In[102]:


A = pd.DataFrame([{'a':1, 'b' : 2}, {'b' : 2, 'c' :3}])


# In[103]:


A


# In[104]:


A.fillna(0)


# In[105]:


A.dropna()


# In[106]:


A


# In[107]:


# implicit vs explicit index


# In[108]:


data = pd.Series(['a','b','c'], index = [1,3,5])


# In[109]:


data[1:3]


# In[112]:


#implicit
data.loc[1:3]


# In[113]:


#explicit( the one)
data.iloc[1:3]


# In[115]:


# mainpulate, read and get the data in cvs file
# sklearn from missing data


# In[118]:


from sklearn.impute import SimpleImputer


# In[5]:


data = pd.read_csv(r'C:\Users\akpla\Desktop\covidData.csv')


# In[6]:


data.head(10)


# In[128]:


#axis  = 1 for columns, inplace = True to reflect all the changes in the data
data.drop(['deathProbable', 'hospitalizedCurrently'], axis= 1,inplace = True)


# In[129]:


data


# In[139]:


data.rename(columns = {'state':'St', 'death':'D'}, inplace = True)


# In[140]:


data.head()


# In[141]:


data['date'] = pd.to_datetime(data['date'])


# In[142]:


data


# In[143]:


#stats
data.describe()


# In[144]:


# see the missing data
data.info()


# In[146]:


data = data.fillna('NA')


# In[147]:


data.info()


# In[4]:


import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


# In[8]:


data.info()


# In[12]:


data = data.fillna('NA')


# In[13]:


data.info()


# In[14]:


data.head(10)


# In[18]:


data2 = data.groupby('state')[['deathConfirmed','hospitalized','hospitalizedCurrently']].sum().reset_index()


# In[23]:


data3 = data[int(data['death'])> 5400]


# # Matplotlib for visualisation

# In[26]:


import matplotlib.pyplot as plt


# In[31]:


#Line plot
x = np.linspace(0,10,1000)
y = np.sin(x)
plt.plot(y)


# In[36]:


# Scatter Plot
plt.scatter(x[::10],y[::10], color = 'red')


# In[40]:


plt.plot(x,y, color = 'red')
plt.plot(x,np.cos(x), color = 'green')


# In[ ]:




