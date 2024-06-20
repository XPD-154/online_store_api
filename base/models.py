from django.db import models

# Create your models here.

# model for supplier
class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True)
    supplier_id = models.CharField(max_length=200, null=True)
    contact_information = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# model for inventory   
class Inventory(models.Model):
    name = models.CharField(max_length=200, null=True)
    item_id = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



