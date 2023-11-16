from django.db import models


# Create your models here.
# This is a table in MySQL database.
# models.Model - Model stands for a table in the DB
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        db_table = 'products'
