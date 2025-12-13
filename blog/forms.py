from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    """User registration form with email"""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    """Form to create / edit posts"""

    class Meta:
        model = Post
        fields = ["title", "excerpt", "content", "image", "published"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.Textarea(
                attrs={"class": "form-control", "rows": 2}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 6}
            ),
            "published": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }
