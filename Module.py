#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def CheckIfNotNumeric(*args):
    RetValue = True
    for x in args:
        if not(isinstance(x, (int, float))):
            return False
        return True
def addAllNumeric(* args):
    sum = 0
    for x in args:
        sum += x
    return sum

myName = "Python Course"

