#!/usr/bin/env python
# coding: utf-8

# In[ ]:


names = ["Aaden", "Aaliyah", "Aarav", "Aaron", "Ab", "Abagail", "Abb", "Abbey", "Abbie", "Abbigail", "Abbott", "Abby", "Abdiel", "Abdul", "Abdullah", "Abe", "Abel", "Abelardo", "Abie", "Abigail"]
check = input("Enter your favorite character      ")
if check not in names:
    print("")
    check = input(check + "  not on list sorry. Please enter again   ") 
else:
    if check == "John" or check == "James" or check == "Jona":
        print(check + " " "is also my favorite character   ")

