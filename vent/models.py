from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Accounts(models.Model):
  fname = models.CharField(max_length= 50)
  lname = models.CharField(max_length=50)
  username =models.CharField(max_length=50)
  email = models.CharField(max_length=60)
  password = models.CharField(max_length=90)
  acctb= models.CharField(max_length=100,default=0)

  #plans table in the data base

class Investment_plans(models.Model):
    plan_name= models.CharField(max_length=50)
    increase_price = models.CharField(max_length=10)
    max_deposit = models.CharField(max_length=1000)
    duration = models.CharField(max_length=100)


    #history tables in the database

#plans history 
class Activated_plans(models.Model):
    planName = models.CharField(max_length=50)
    profit =models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    depositedAmount =models.CharField(max_length=50)
    adate = models.DateTimeField(default=datetime.now ,blank=True)
    status =models.CharField(max_length=20, default="Active")
    usern= models.CharField(max_length=50)

class Withdrawals(models.Model):
   amount=models.CharField(max_length=1000)
   status = models.CharField(max_length=1000, default='Request Accepted: Processing') 
   accountnumber = models.CharField(max_length=1000)
   user_requested =models.CharField(max_length=50)


class Deposit_request(models.Model):
   amount = models.IntegerField()
   user_requested = models.CharField(max_length=100)
   bitcoin_amount=models.CharField(max_length=10000)
   date= models.DateTimeField(default=datetime.now, blank=True)


class Coin_rate(models.Model):
   bitcoin = models.CharField(max_length=10000, default=0.000023)


class Admin_account_no(models.Model):
   acctn= models.CharField(max_length=100000)

