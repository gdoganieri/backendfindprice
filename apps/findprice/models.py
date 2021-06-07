import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
User = get_user_model()
CATEGORY_CHOICES =  (
    ('undefined','UNDEFINED'),
    ('alimenti', 'ALIMENTI'),
    ('giocattoli','GIOCATTOLI'),
    ('elettronica','ELETTRONICA'),
    ('casa','CASA')
)



class Product(models.Model):
    product_name= models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200,default= 'undefined', choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.product_name, self.category)


class Scan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = UserForeignKey(auto_user_add=True, blank = True, verbose_name="The user that is automatically assigned", related_name="mymodels")
    scan_time = models.DateTimeField(auto_now_add=True, blank= True)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=9, decimal_places=7)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return "{}, {}".format(self.product, self.price)



