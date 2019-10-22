from django.db import models

# Create your models here.

#class HoursInDay():
	#day
	#hours, list of times open on that day

#class HoursOfOp(models.Model):
	#service
	#hours = HoursInDay
	#updated, when this updated it will send a post to the forum telling people that the hours have changed

class FAQ(models.Model):
	question = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.question

class Rule(models.Model):
	rule = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.rule
