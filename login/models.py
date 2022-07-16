from django.db import models

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    #email = models.EmailField(max_length=255, null=False)
    user_type=models.CharField(max_length=50)
    mobile=models.BigIntegerField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password= models.CharField(max_length=50,null=True)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")
    created_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    updated_date = models.DateTimeField(auto_now=True, null=False, blank=False)


    def __str__(self):
        return self.mobile


""" User Input"""
from django.db import models

# Create your models here.
class Input(models.Model):
    farmers_name = models.CharField(max_length=255, null=False)
    total_amt_paid = models.CharField(max_length=255,null=False)
    payment_method = models.CharField(max_length=255,null=False)
    date=models.DateTimeField(auto_now_add=True, null=False, blank=False)

    # def __str__(self):
    #     return self.farmers_name


"""weight"""
class Manual_Weight(models.Model):
    sub_dealer_name=models.CharField(max_length=100,null=False)
    weight_type=models.CharField(max_length=100,null=False)
    gross_weight=models.CharField(max_length=100,null=False)
    gunny_bag_weight=models.CharField(max_length=100,null=False)
    rate=models.CharField(max_length=100,null=False)
    total_amount = models.CharField(max_length=100,null=False)
    date=models.DateField(auto_now=True, null=False, blank=False)

class Direct_Weight(models.Model):

    sub_dealer_name=models.CharField(max_length=100,null=False)
    weight_type=models.CharField(max_length=100,null=False)
    net_weight=models.CharField(max_length=100,null=False)
    rate=models.CharField(max_length=100,null=False)
    total_amount = models.CharField(max_length=100,null=False)
    date=models.DateField(auto_now=True, null=False, blank=False)

    


'''Quantity'''
class Quantity(models.Model):
    quantity = models.CharField(max_length=100,null=False)
    rate=models.CharField(max_length=100,null=False)
    total_amount = models.CharField(max_length=100,null=False)
    date=models.DateField(auto_now=True, null=False, blank=False)
