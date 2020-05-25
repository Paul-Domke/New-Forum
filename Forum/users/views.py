from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from posts.models import Post

def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	user = request.user
	context={
		'user': user,
		'posts': Post.objects.filter(author = user)
	}
	return render(request, 'users/profile_page.html', context)
