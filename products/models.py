from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
from datetime import datetime, date


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name 

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


    
