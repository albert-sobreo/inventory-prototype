from django.db import models
from django.db.models.fields import EmailField
from decimal import Decimal
from django.db.models import Avg, Max, Min, Sum

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
    cost_per_item = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    turnover = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.code + ' ' + self.name

    @property
    def cost_sold(self):
        #"%.2f" % a
        cost_of_good_sold = self.sales_item_set.filter(sales_order__approved=True).aggregate(total=Sum('total_cost'))
        return cost_of_good_sold

    @property
    def quantity_sold(self):
        quantity_sold = self.sales_item_set.filter(sales_order__approved=True).aggregate(total=Sum('sales_quantity'))
        return quantity_sold

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    owner_first_name = models.CharField(max_length=255, null=True, blank=True)
    owner_last_name = models.CharField(max_length=255, null=True, blank=True)
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
    owner_last_name = models.CharField(max_length=255, null=True, blank=True)
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
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    approved = models.BooleanField()
    total_amount_due = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.ref_id

class Purchase_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    purchase_quantity = models.IntegerField()
    cost_per_item = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Sales_Order(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    approved = models.BooleanField()
    total_amount_due = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.ref_id

class Sales_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_order = models.ForeignKey(Sales_Order, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    sales_quantity = models.IntegerField()
    cost_per_item = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Transfer(models.Model):
    ref_id = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

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
    approved = models.BooleanField(default=False)
    total_lost = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.ref_id

class Spoilage_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    spoilage = models.ForeignKey(Spoilage, on_delete=models.CASCADE)
    remaining = models.IntegerField()
    spoilage_quantity = models.IntegerField()
    reason = models.TextField()
    cost_per_item = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=24, decimal_places=5, null=True, blank=True)

    def __str__(self):
        return self.product.code + ' ' + self.product.name

class Branch(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.ManyToManyField(Vendor)
    customer = models.ManyToManyField(Customer)
    purchase_order = models.ManyToManyField(Purchase_Order)
    sales_order = models.ManyToManyField(Sales_Order)
    transfer = models.ManyToManyField(Transfer)
    spoilage = models.ManyToManyField(Spoilage)
    product = models.ManyToManyField(Product)
    warehouse = models.ManyToManyField(Warehouse)