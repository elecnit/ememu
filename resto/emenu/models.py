from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):
    item_cat = models.CharField(max_length=200)

    def __str__(self):
        return self.item_cat


class FoodItems(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self): # new
           return reverse('detailfood', args=[str(self.id)] )



class order(models.Model):
     order_items = models.CharField(max_length=300)
     table_no = models.IntegerField(null=True,blank=True)
     customer_id = models.IntegerField()
     served = models.BooleanField(default=False)
     
