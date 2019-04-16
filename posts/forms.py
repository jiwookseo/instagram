from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={
                    'rows': 7,
                    'placeholder': '오늘은 무엇을 하셨나요'
                }))
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ('content', 'image',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '댓글 입력'}))
    class Meta:
        model = Comment
        fields = ('content',)
