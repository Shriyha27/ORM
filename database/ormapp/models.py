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
