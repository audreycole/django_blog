from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    # Return a string representation of the question
    def __str__(self):
		return self.name

class Post(models.Model):
	#author = models.ForeignKey('auth.User')
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

