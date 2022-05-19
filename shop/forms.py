
from .models import Comment, Comments
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user_nickname', 'comment_date', 'id']
        widgets = {'text':TextInput(attrs={'class':'form-control', 'placeholder' : 'Добавить комментарий'}), 'user_nickname':TextInput(attrs={'class':'form-control', 'placeholder' : 'Имя'}), 'comment_date':TextInput(attrs={'class':'form-control', 'placeholder' : 'дата'})}


class CommentsForm(M):