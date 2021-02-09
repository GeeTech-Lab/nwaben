from django_summernote.admin import SummernoteModelAdmin
from django.db import models
from django.contrib import admin
from .models import Article, Comment, Category, Reply

# from pagedown.widgets import AdminPagedownWidget
# Register your models here.

admin.site.register(Category)


# Apply summernote to all TextField in model.
# class SummerNoteModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'category')
    list_filter = ('author', 'created', 'created', 'category')
    search_field = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('by', 'content', 'approved')


admin.site.register(Comment, CommentAdmin)


# class ReplyAdmin(admin.ModelAdmin):
#     list_display = ('replied_by', 'content')
#
# admin.site.register(Reply, ReplyAdmin)
