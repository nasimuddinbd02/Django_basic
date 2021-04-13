from django.db import models


class Brand(models.Model):
    Code=models.CharField(max_length=100)
    Name=models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Category(models.Model):
    Code=models.CharField(max_length=100)
    Name=models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Code=models.CharField(max_length=100)
    Name=models.CharField(max_length=200)
    Description =models.CharField(max_length=250)
    Brand =models.ForeignKey(Brand, related_name='Products',  on_delete=models.CASCADE)
    Category=models.ForeignKey(Category, related_name='Brands', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

