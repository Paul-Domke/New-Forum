from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
from django import forms


class Tag(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=100)
	post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
	date_posted = models.DateTimeField(default=timezone.now)
	last_edit = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment

class Report(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='reports')

	def __str__(self):
		return self.author.username

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE) # Deletes post when user is deleted, will want to change so post dosent get removed 
	subject = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	last_edit = models.DateTimeField(auto_now=True)
	locked = models.BooleanField(default=False)

	tags = models.ManyToManyField('posts.Tag', related_name='tags')
	
	#comments = models.ManyToManyField('posts.Comment', related_name='posts')
	#reports = models.ManyToManyField('posts.Report', related_name='posts')
	upvotes = models.ManyToManyField(User, related_name="upvotes")
	#reacts

	def __str__(self):
		return self.subject


	def get_absolute_url(self):
		return reverse('posts-detail', kwargs={'pk': self.pk})

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']