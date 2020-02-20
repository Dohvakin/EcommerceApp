from django.db import models
from EcommerceApp.models import UserProfile
# Create your models here.

class Category(models.Model):
	cat = models.CharField(max_length=30)


class Products(models.Model):
	product_name = models.CharField(max_length=30)
	product_desc = models.CharField(max_length=50)
	product_price = models.DecimalField(decimal_places=2, max_digits=10)
	added_by_seller = models.CharField(max_length=30)
	product_img = models.ImageField(upload_to='productimage', blank=True)
	product_avail = models.IntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
