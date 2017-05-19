
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=200)
    user = models.ManyToManyField(User, related_name ='courses')


class Post(models.Model):
    post = models.CharField(max_length=300)     
    pub_time = models.DateTimeField(auto_now_add=True)  
    course = models.ForeignKey(Course, related_name='posts', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) 
     

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    pub_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
