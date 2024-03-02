from django.urls import path
from . import views    

app_name = 'orderapp'

urlpatterns = [
    path('', views.menuitem_list, name='menuitem_list'),
    path('home', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:menuitem_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
]