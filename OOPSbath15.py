#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Dog:
    def __init__(self, name, old, numid):
        self.name = name
        self.old = old 
        self.numid = numid
    def display(self):
        print(self.name)
        print(self.old)
        print(self.numid)
    def details(self):
        print("my name is {}".format(self.name))
        print("Old: {}".format(self.old))
        print("Numid is: {}".format(self.numid))
class child(Dog):
    def __init__(self, name, old, numid, parent):
        self.parent = parent
        Dog.__init__(self, name, old, numid)
    def details(self):
        print("my name is {}".format(self.name))
        print("Old: {}".format(self.old))
        print("Numid is: {}".format(self.numid))
        print("Parents: {}".format(self.parent))
Sun = Dog("Sun", 9, 231)
Moon = child("Moon", 3, 536, "Sun")
Moon.details()
Sun.details()
Sun.display()


# In[ ]:




