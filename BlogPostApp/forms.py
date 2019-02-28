from .models import BlogPostModel
from django.forms import ModelForm


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ["title", "text"]
