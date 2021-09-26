from django.db import models

class Car(models.Model):
    pruduct_nman = models.CharField(max_length= 100)
    pruduct_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
     
