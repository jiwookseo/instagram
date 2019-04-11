from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={
                    'rows': 7,
                    'placeholder': '오늘은 무엇을 하셨나요'
                }))
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ('content', 'image',)
