from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=255)
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
    turnover = models.DecimalField(max_digits=3, decimal_places=2)
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
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    approved = models.BooleanField()

class Purchase_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    purchase_quantity = models.IntegerField()

class Sales_Order(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    approved = models.BooleanField()

class Sales_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_order = models.ForeignKey(Sales_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    sales_quantity = models.IntegerField()

class Transfer(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

class Transfer_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    transfer_quantity = models.IntegerField()

class Spoilage(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()

class Spoilage_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    spoilage = models.ForeignKey(Spoilage, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    spoilage_quantity = models.IntegerField()
    reason = models.TextField()