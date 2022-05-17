
from .models import Comment
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user_nickname', 'comment_date', 'id']
        widgets = {'text':TextInput(attrs={'class':'form-control', 'placeholder' : 'Добавить комментарий'}), 'user_nickname':{{ User.username }}, 'comment_date':TextInput(attrs={'class':'form-control', 'placeholder' : 'дата'})}