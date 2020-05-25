from django.db import models
from django.contrib.auth.models import User
from posts.models import Tag
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from django import forms

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class SubscribeForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['subs']