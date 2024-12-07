from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget
from .models import Post, Comment,Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Use the TagWidget for the tags field
        }
       

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data.get('tags', '')
        if commit:
            instance.save()
            if tags:
                tag_names = [tag.strip() for tag in tags.split(',')]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    instance.tags.add(tag)
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'content': 'Write your comment here:',
        }
  
