
from django.db import models
from django.db.models.deletion import SET


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField()
    stock = models.IntegerField()
    sku = models.CharField(max_length=15)
    brand = models.CharField(max_length=20, null=True)
    
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Cart(models.Model):
    pass
    #products = models.ManyToManyField(Product, through=CartItem)

class CartItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
