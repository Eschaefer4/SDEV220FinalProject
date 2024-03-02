from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import MenuItem, CartItem, Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

def menuitem_list(request):
    menuitems = MenuItem.objects.all()
    return render(request, 'orderapp/index.html', {'menuitems': menuitems})

# login is REQUIRED to do anything with cart.
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menuitem.price * item.quantity for item in cart_items)
    return render(request, 'orderapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, menuitem_id):
    menuitem = MenuItem.objects.get(id=menuitem_id)
    cart_item, created = CartItem.objects.get_or_create(menuitem=menuitem, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('orderapp:view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('orderapp:view_cart')

# view profile for current user
@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'orderapp/view_profile.html', {'profile':profile})

# edit a profile by changing name and/or email
@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return render(request, 'orderapp/view_profile.html', {'profile':profile})
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'orderapp/edit_profile.html', {'form': form})

def home(request):
    return HttpResponse('Hello, World!')
