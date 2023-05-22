from django.contrib import admin

from .models import Category , FoodItems , order
# Register your models here.
admin.site.register(Category)
admin.site.register(FoodItems)
admin.site.register(order)


