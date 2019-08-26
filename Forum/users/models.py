from django.db import models
from django.contrib.auth.models import User
from posts.models import Tag

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	banned = models.BooleanField(default=False)
	subs = models.ManyToManyField('posts.Tag', related_name='profiles')

	#accountType =
	#blocked users =
	#Banned until =
	#Ban History =

	def __str__(self):
		return self.user.username