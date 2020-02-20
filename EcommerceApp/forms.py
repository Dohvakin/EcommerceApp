from django import forms
from django.contrib.auth.models import User
from EcommerceApp.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	CHOICES= (('Buyer', 'Buyer'),('Seller', 'Seller'),)
	usertype = forms.CharField(widget=forms.Select(choices=CHOICES))
	class Meta():
		model = UserProfile
		fields = ('mobile', 'usertype')
		