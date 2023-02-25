from .models import Comment, Post, Contact
from django import forms
from django.forms import ModelForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
