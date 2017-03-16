from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Driver(models.Model):
	driver_number = models.CharField(max_length=14,primary_key = True)
	name = models.CharField(max_length=100)
	status = models.CharField(max_length=100)
	usesApp = models.BooleanField(default=False)
	password = models.CharField(max_length=50)


	def __str__(self):
		return self.name


