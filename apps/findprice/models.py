from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Product(models.Model):
    product_name= models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200,default= 'Undefined')
    description = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.product_name, self.category)