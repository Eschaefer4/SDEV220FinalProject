from django.contrib import admin
from .models import MenuItem, CartItem, Profile
# note:
# admin username is bobuser
# admin pw is bobburger
# test non admin name is testnonadmin
# test non admin pw is winner46
admin.site.register(MenuItem)
admin.site.register(CartItem)
admin.site.register(Profile)