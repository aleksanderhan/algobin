from __future__ import unicode_literals

from django.db import models


class Algorithm(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=600)
	pub_date = models.DateTimeField('date published')


class LineOfCode(models.Model):
	algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
	lineText = models.CharField(max_length=150)