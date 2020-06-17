from django import forms
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
        widgets = {
            'image': forms.FileInput(attrs={'class': 'btn btn-raised btn-round btn-default btn-file'}),
        }


class CategoryForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Category
        fields = ("name",)


class CommentForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('content',)


class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'reply this comment', 'rows': '3'}), label="",)

    class Meta:
        model = Reply
        fields = ("content",)
