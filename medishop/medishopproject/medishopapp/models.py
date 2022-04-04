
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    img=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='product',blank=True)




    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)