from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = [
            "username", "email", "password1", "password2"
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = [
            "username", "email"
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] # author set automatically in view
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write post content...'}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
        }