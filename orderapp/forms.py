from django import forms

from .models import Profile
# Form for editing profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'email',)