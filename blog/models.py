from django.urls import reverse
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    auther=models.ForeignKey('auth.User',on_delete=models.CASCADE) #foreignkey bec (one on to many) as one auther can have many posts
    body=models.TextField()
    def __str__(self):
        return self.title   
    def get_absolute_url(self): # reverse is redirect the page to another one using get_absolute_url
        return reverse('post_detail', args=[str(self.id)])  