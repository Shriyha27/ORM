# Ex02 Django ORM Web Application
# Date: 25.03.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2025-03-18 113603.png>)
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
    cus_id=models.CharField(max_length=100,primary_key = True)
    cus_name=models.CharField(max_length=100)
    bankloan_no=models.IntegerField()
    bankloan_amt=models.IntegerField()
    dateofissue=models.DateField()
    email=models.EmailField()
class userAdmin(admin.ModelAdmin):
    list_display=['cus_id','cus_name','bankloan_no','bankloan_amt','dateofissue','email']
```
```
admin.py

from django.contrib import admin
from .models import BankLoan,userAdmin
admin.site.register(BankLoan,userAdmin)
```
# OUTPUT
![alt text](<Screenshot (111).png>)
![alt text](<Screenshot (112).png>)
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
