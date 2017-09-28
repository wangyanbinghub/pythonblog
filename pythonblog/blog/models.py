#blog/models.py
#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#分类
class Category(models.Model):
    name = models.CharField(max_length=100)

#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

#文章
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

