from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    title=models.CharField(max_length=20)
    topic=models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now=True)
class Entry_md(models.Model):
    title=models.CharField(max_length=20)
    topic=models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL)
    text=MDTextField()
    date_added=models.DateTimeField(auto_now=True)