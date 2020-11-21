from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    size = models.CharField(max_length=10)
    amount = models.IntegerField()
    brand = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ["date"]

    def __str__(self):
        return self.name


# Create your models here.


"""
picture
color 
quantity
weight
amount
shipping time 
picture
Brand
"""