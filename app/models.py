from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    auth_level = models.CharField(max_length=255)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Product(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    turnover = models.DecimalField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landline = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    bank = models.CharField(max_length=255) 
    bank_number = models.CharField(max_length=255)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landline = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    bank = models.CharField(max_length=255) 
    bank_number = models.CharField(max_length=255)

class Purchase_Order(models.Model):
    