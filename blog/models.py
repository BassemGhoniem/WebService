from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.



# class User(AbstractUser):
# 	pass

class Post(models.Model):
	author = models.ForeignKey(User , related_name='posts')
	title  = models.CharField(max_length=100)
	body   = models.TextField(blank =True  , null=True)

		     