from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

from articles.models import Article, Comment, Category, Reply


class ArticleForm(forms.ModelForm):
    category = forms.CharField(label='Category')

    class Meta:
        model = Article
        fields = ("category",
                  "title",
                  "description",
                  "image",
                  "body",
                  "draft",)
        # widgets = {
        #     'description': SummernoteWidget(),
        #     'body': SummernoteWidget(),
        # }


class CategoryForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Category
        fields = ("name",)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget(),
        }


class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'reply this comment', 'rows': '3'}), label="",)

    class Meta:
        model = Reply
        fields = ("content",)
