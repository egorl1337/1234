
from .models import Comment
from django.forms import ModelForm, TextInput



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user_nickname', 'comment_date', 'id']
        widgets = {'text':TextInput(attrs={'class':'form-control', 'placeholder' : 'Добавить комментарий'}), 'user_nickname':TextInput(attrs={'class':'form-control', 'placeholder' : 'ник'}), 'comment_date':TextInput(attrs={'class':'form-control', 'placeholder' : 'дата'})}