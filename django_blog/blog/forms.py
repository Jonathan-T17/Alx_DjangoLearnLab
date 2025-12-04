from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post
from django import forms
from .models import Comment, Tag


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
    # Extra field for tags (comma-separated)
    tags_field = forms.CharField(
        required=False,
        help_text="Enter comma-separated tags",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "django, python, tutorial"
        })
    )

    class Meta:
        model = Post
        fields = ["title", "content"]  # author set automatically in view
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter post title"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write post content..."
            }),
        }
        labels = {
            "title": "Title",
            "content": "Content",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prepopulate tags_field if editing an existing post
        if self.instance.pk:
            current_tags = self.instance.tags.all().values_list("name", flat=True)
            self.fields["tags_field"].initial = ", ".join(current_tags)

    def clean_tags_field(self):
        raw = self.cleaned_data.get("tags_field", "")
        tags = [t.strip() for t in raw.split(",") if t.strip()]
        # remove duplicates while preserving order
        return list(dict.fromkeys(tags))

    def save(self, commit=True):
        post = super().save(commit=commit)
        tags_list = self.cleaned_data.get("tags_field", [])

        tag_objects = []
        for tag_name in tags_list:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag_obj)

        post.tags.set(tag_objects)
        return post






class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        label='',
        max_length=2000
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
