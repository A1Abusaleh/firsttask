from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
#from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import UUIDField



class Post(models.Model):
    title = models.CharField(max_length=100, default="your book's title")
    uuid = models.UUIDField
    author = models.ForeignKey(User, on_delete= models.CASCADE,)    
    creation_date = models.DateTimeField(auto_now_add=True)  
    publication_date = models.IntegerField


class writer(models.Model):

	name = models.CharField(max_length=100)
	coutry = models.CharField(max_length=200)
	uuid = models.UUIDField
	
    
class Meta:
    ordering = ['-creation_date']

def __str__(self):
	return self.title
