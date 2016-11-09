from __future__ import unicode_literals

from django.db import models


class Algorithm(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=600)
	pub_date = models.DateTimeField('date published')
	vote = models.IntegerField(default=0)

	def __str__(self):
		return name


class LineOfCode(models.Model):
	algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
	line = models.CharField(max_length=150)

	def __str__(self):
		return line