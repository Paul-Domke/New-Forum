from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Report, Comment, Tag, PostForm, CommentForm
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DetailView,
	RedirectView,
)
from users.models import Profile, SubscribeForm
from django.template import RequestContext
from django.db.models import Count


@login_required
def home(request):
	subList = list(Profile.objects.get(user = request.user).subs.all())
	subPost = Post.objects.filter(tags__title__in= subList).distinct()

	context={
		'posts': Post.objects.all().order_by('-date_posted'),
		'subs': subPost.order_by('-date_posted'),
		'trends': Post.objects.all().annotate(num_tags = Count('upvotes') ).order_by('-num_tags'),
		'tags': Tag.objects.all(),
		'count': Post.objects.count(),
	}
	return render(request, 'posts/home.html', context)

@login_required
def tagFilter(request, tag):
	context={
		'posts': Post.objects.filter(tags__title= tag),
		'tags': Tag.objects.all(),
	}
	return render(request, 'posts/home.html', context)

def settings(request):
	return HttpResponse('<h1>settings</h1>')

class PostUpvote(RedirectView):
    def get_redirect_url(self, *args ,**kwargs):

        obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        url_ = obj.get_absolute_url() 
        user = self.request.user
        if user is not None:
        	listobj = obj.upvotes.all()
        	if user in listobj.iterator():
        		obj.upvotes.remove(user)
        	else:
        		obj.upvotes.add(user)

        return url_


def PostDetailView(request, pk):
	context = {
		'tags': Tag.objects.all(),
		'post': Post.objects.get(pk = pk)
	}
	return render(request, 'posts/post_detail.html', context)

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	#fields = ['subject', 'content', 'tags']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['subject', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#def SubscribedPage(request):

def AddCommentToPost(request, pk):
	
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('posts-detail', pk=post.pk)
	else:
		form = CommentForm()
		context = {
		'tags': Tag.objects.all(),
		'post': Post.objects.get(pk = pk),
		'form': form
		}	
		return render(request, 'posts/add_comment.html', context)

def search(request):
	query = request.GET.get('q')
	results = Post.objects.filter(Q(subject__icontains=query) | Q(content__icontains=query))

	subList = list(Profile.objects.get(user = request.user).subs.all())
	subPost = Post.objects.filter(tags__title__in= subList).distinct()

	context = {
		'posts' : results,
		'subs': subPost.order_by('-date_posted'),
		'trends': Post.objects.all().annotate(num_tags = Count('upvotes') ).order_by('-num_tags'),
		'tags': Tag.objects.all(),
		'count': Post.objects.count(),
	}

	return render(request, 'posts/home.html', context)

def TagSubscribe(request):
	if request.method == "POST":
		form = SubscribeForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.tags = tags
			profile.save()
			return redirect('posts-home')
	else:
		form = SubscribeForm()
		context = {
		'tags': Tag.objects.all(),
		'form': form
		}	
		return render(request, 'posts/subscribe_tag.html', context)
