#!/usr/bin/env python
# coding: utf-8

# In[1]:


FirstName=str(input("Write your first name: "))
LastName=str(input("Write your last name: "))
print(LastName + " " + FirstName)


# In[2]:


Num=int(input("Enter a number between 1 and 9: "))
Num1=Num+(Num*10)
Num2=Num1+(Num*100)
S=Num+Num1+Num2
print(S)


# In[3]:


Num=int(input("Enter a number : "))
if Num % 2==0:
    print("Your number is even")
else:
    print("Your number is odd ")


# In[4]:


for i in range(2000,3201):
    if i % 7==0 and i % 5!=0:
        print(i)
    
    


# In[8]:


Num=int(input("Enter a number: "))
f = 1
for i in range(1,Num+1):
    f=f*i
print(f)



# In[ ]:


str1=str(input("Enter a string: ")
for i in str1:
if str[i]%2=0:
         print(i)
         


# In[ ]:


Price=int(input("enter a price: "))
if Price >=500:
    Price=Price/2
elif Price >=200 and Price <=500:
    Price=(Price*70)/100
elif Price < 200:
    Price=(Price*90)/100


# In[ ]:




