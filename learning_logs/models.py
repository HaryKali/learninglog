from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    #TODO:添加小标题
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now=True)