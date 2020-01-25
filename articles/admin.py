from django.contrib import admin

# Register your models here.
from articles.models import Category, Article, Comment

admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'category')
    list_filter = ('author', 'created', 'created', 'category')
    search_field = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
# formfield_overrides = {


#     models.TextField: {'widget': AdminPagedownWidget },
# }

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('by', 'content', 'approved')


admin.site.register(Comment, CommentAdmin)
