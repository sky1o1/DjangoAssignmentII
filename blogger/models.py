from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='pro_pic/', blank=True, null=True)
    bio = models.TextField(max_length=200, default='No bio')


class BlogTable(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title



