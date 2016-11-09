from __future__ import unicode_literals

from django.db import models


class Algorithm(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	language = models.CharField(max_length=20)
	code = models.TextField()
	pub_date = models.DateTimeField('date published')
	vote = models.IntegerField(default=0)

	def __str__(self):
		return name


class Tag(models.Model):
	algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
	tag = models.CharField(max_length=20)