from django.db import models

from userauth.models import rudeusers
from userauth.models import rudeusers


class usersData(models.Model):
    user_id = models.ForeignKey(rudeusers, on_delete=models.CASCADE , default= None)
    trade_id = models.AutoField
    action =  models.CharField(max_length=10,default=None)
    market =  models.CharField(max_length=10,default=None)
    symbol =  models.CharField(max_length=20,default=None)
    quantity =  models.FloatField(default=None)
    entry_datetime = models.DateTimeField(default=None)
    exit_datetime =  models.DateTimeField(default=None)
    entry_price =  models.FloatField(default=None)
    exit_price =  models.FloatField(default=None)
    entry_reason =  models.CharField(max_length=200,default=None)
    follow_setup =  models.CharField(max_length=5,default=None)
    trade_note =  models.CharField(max_length=5000,default=None)
    pnl =  models.FloatField(default=None)
    trade_rating =  models.IntegerField(default=None)


class user_daily_pnl(models.Model):
    
    trade_date_id=models.AutoField 
    user_id = models.ForeignKey(rudeusers, on_delete=models.CASCADE , default= None)
    entry_datetime = models.DateField(default=None)
    daily_pnl =  models.FloatField(default=None)