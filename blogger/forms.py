from django.forms import ModelForm
from .models import  BlogTable


class BlogForm(ModelForm):
    class Meta:
        model = BlogTable
        fields = ['title', 'blog']