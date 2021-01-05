from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    auth_level = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    turnover = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.code + ' ' + self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255, null=True, blank=True)
    owner_first_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    landline = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    bank = models.CharField(max_length=255, null=True, blank=True) 
    bank_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255, null=True, blank=True)
    owner_first_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    landline = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    bank = models.CharField(max_length=255, null=True, blank=True) 
    bank_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Purchase_Order(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    approved = models.BooleanField()

    def __str__(self):
        return self.ref_id

class Purchase_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    purchase_quantity = models.IntegerField()

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Sales_Order(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    approved = models.BooleanField()

    def __str__(self):
        return self.ref_id

class Sales_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_order = models.ForeignKey(Sales_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    sales_quantity = models.IntegerField()

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Transfer(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.ref_id

class Transfer_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    transfer_quantity = models.IntegerField()

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Spoilage(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.ref_id

class Spoilage_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    spoilage = models.ForeignKey(Spoilage, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    spoilage_quantity = models.IntegerField()
    reason = models.TextField()

    def __str__(self):
        return self.product.code + ' ' + self.product.name