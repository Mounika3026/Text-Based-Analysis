#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Hello"
print(a)


# In[3]:


a = "Hello, World!"
print(a[1])


# In[5]:


b = "Hello, World!"
print(b[2:5])


# In[6]:


a = "Hello"
b = "World"
c = a+""+b
print(c)


# In[8]:


a.isalnum()


# In[9]:


a.isalpha() 


# In[10]:


a.isupper()


# In[12]:


b.isspace()


# In[13]:


a.lstrip()


# In[16]:


a.strip()


# In[25]:


e = "Hello World"
e.lstrip("H")


# In[27]:


e.strip("")


# In[28]:


e.endswith("World")


# In[29]:


e.startswith("World")


# In[33]:


e.find("W")


# In[34]:


name_a="                      old is gold"
name_a.lstrip()


# In[39]:


f="peter is a prince"
f.replace("prince","king")


# In[41]:


my_list = 'one two three'
word_list = my_list.split()
word_list


# In[43]:


my_list2 = '4/6/2024'
word_list2 = my_list2.split('/')
word_list2


# In[44]:


address = "www.example.com"
tokens = address.split('.')
tokens


# In[53]:


import regex as re
def tokenize(text):
    return re.findall(r'a', text)
x = tokenize("abcd 45abc abc% abc.com acbrx .=.abc.=. ab c cba ABC ")
x


# In[51]:


import regex as re
def tokenize(text):
    return re.findall(r'.oo.y', text)
x = tokenize(" abcd gooey moody broody goofy gummy mooooudy loopy ooy ")
x


# In[58]:


import regex as re
def tokenize(text):
    return re.findall(r'abc\.abc.com', text)
x = tokenize("abc.abc.com abc.abc,com abc,abc.com ABC.abc.com ")
x


# In[59]:


import regex as re
def tokenize(text):
    return re.findall(r'^The', text)
x = tokenize("Them ")
print(x)
y= tokenize("them")
print(y)


# In[60]:


import regex as re
def tokenize1(text):
    return re.findall(r'Homer Simpson|Marge Simpson', text)
def tokenize2(text):
    return re.findall(r'(Homer|Marge) Simpson', text)
x = tokenize1("Homer Williams Homer Simpson Marge Simpson")
print(x)
x = tokenize2("Homer Williams Homer Simpson Marge Simpson")
print(x)


# In[65]:


import regex as re
def tokenize(text):
    return re.findall(r'abc*', text)
x = tokenize("abcd ab abcccc acb abbbbc abcccccccc fabulous")
print(x)


# In[ ]:




