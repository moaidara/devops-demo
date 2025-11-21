from pyexpat import model
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100);
    price = models.FloatField();
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

