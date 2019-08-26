from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	New_College_Email_Address = forms.EmailField()

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'New_College_Email_Address']
