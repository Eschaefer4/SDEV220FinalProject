from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# Standard class for a menu item
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/menuitems/')
 
    def __str__(self):
        return self.name

# Keep track of what users have how much of each item in their carts
class CartItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.quantity} x {self.menuitem.name}'

# model to handle user profiles beyond the basic Django user stuff
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='John Doe')
    email = models.EmailField(max_length=254, blank=True, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'