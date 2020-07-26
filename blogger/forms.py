from django.forms import ModelForm
from .models import BlogTable, UserDetail
from django.contrib.auth.models import User


class BlogForm(ModelForm):
    class Meta:
        model = BlogTable
        fields = ['title', 'blog']


class AuthorForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class EditForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['bio', 'profile_pic']