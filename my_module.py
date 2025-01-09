#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lambda
greet = lambda name : print(f"Good Morning {name} !")
greet("Soumya")


# In[3]:


# lambda Product
product = lambda a,b,c: a * b * c
result = product(4,5,7) 
print(result)


# In[5]:


# lambda function with list Comprehension
even = lambda L : [x for x in L if x%2 ==0]
my_list = [122,3,8,9,90,86,45]
even(my_list)


# In[ ]:




