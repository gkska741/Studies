from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the Content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '에러 발생'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'

