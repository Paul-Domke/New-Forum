from django.db import models

# Create your models here.


class HoursOpen(models.Model):

	weekday = models.CharField(max_length=10)
	hour_start = models.TimeField()
	hours_end = models.TimeField()

class HoursOfOp(models.Model):
	service = models.CharField(max_length=50)
	hours = models.ManyToManyField('info.HoursOpen', related_name="hours")

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
