from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm

def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})
