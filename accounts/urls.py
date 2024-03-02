from django.urls import path

from .views import SignUpView

# one url for registration
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]