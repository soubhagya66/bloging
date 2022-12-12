from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=["post"]
        labels={
            "user_name":"your name",
            "user_email":"your mail",
            "text":"your comment"

        }