from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post, Report, Comment
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DetailView,
)
from users.models import Profile
from django.template import RequestContext

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'posts/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['subs'] = Profile.objects.all
		return context




class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['subject', 'content', 'tags']

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
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/post_detail.html', {'form': form})