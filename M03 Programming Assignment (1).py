#!/usr/bin/env python
# coding: utf-8

# In[1]:


things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize()
things[0] = things[0].upper()
things.remove("salmonella")

print(things)


# In[8]:


def good():
    print("Harry", "Ron", "Hermoine")

good()


# In[24]:


def get_odds():
    for number in range(1,10,2):
        yield number

count = 1
for number in get_odds():
    if count == 3:
        print("The third odd number is", number)
        break
    count += 1

