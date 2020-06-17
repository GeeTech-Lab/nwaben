from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from .forms import ArticleForm, CommentForm, CategoryForm, ReplyForm
from .models import Category, Article, Comment, Reply


class ArticleList(generic.CreateView, generic.ListView):
    fields = ("category", "title", "description", "image", "body", "draft")
    model = Article
    context_object_name = 'articles'
    paginate_by = 4
    template_name = "articles/article_list.html"


class DashBoard(View):
    def get(self, request, *args, **kwargs):
        view = ArticleList.as_view(template_name="articles/admin_page.html")
        return view(request, *args, **kwargs)


class ArticleDisplay(generic.DetailView, generic.UpdateView):
    fields = ("category", "title", "description", "image", "body", "draft")
    model = Article
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_object(self):
        view_count_obj = super(ArticleDisplay, self).get_object()
        view_count_obj.view_count += 1
        view_count_obj.save()
        return view_count_obj

    def get_context_data(self, **kwargs):
        context = super(ArticleDisplay, self).get_context_data(**kwargs)
        # comment_obj = Comment.objects.get(article=self.get_object())
        comments = Comment.objects.filter(article=self.get_object())
        context['comments'] = comments
        # context['replies'] = Reply.objects.filter(comment=comment_obj)
        context['form'] = CommentForm
        # context['reply_form'] = ReplyForm
        return context


class ArticleComment(LoginRequiredMixin, generic.FormView):
    form_class = CommentForm
    template_name = 'articles/article_detail.html'

    def form_valid(self, form):
        form.instance.by = self.request.user
        article = Article.objects.get(slug=self.kwargs['slug'])
        form.instance.article = article
        form.save()
        return super(ArticleComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.kwargs['slug']})


# class CommentReply(LoginRequiredMixin, generic.FormView):
#     form_class = ReplyForm
#     template_name = 'articles/comment_reply.html'
#
#     def form_valid(self, form):
#         form.instance.replied_by = self.request.user
#         comment = Comment.objects.get(pk=self.kwargs['pk'])
#         form.instance.comment = comment
#         form.save()
#         return super(CommentReply, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('articles:article_detail', kwargs={'slug': self.kwargs['slug']})
#
#
#
# class CommentDisplay(generic.DetailView):
#     model = Comment
#     template_name = "articles/comment_reply.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(CommentDisplay, self).get_context_data(**kwargs)
#         replies = Reply.objects.filter(comment=self.get_object())
#         context['replies'] = replies
#         context['form'] = ReplyForm
#         print(replies)
#         return context


# class CommentDetail(View):
#     def get(self, request, *args, **kwargs):
#         view = CommentDisplay.as_view()
#         return view(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         view = CommentReply.as_view()
#         return view(request, *args, **kwargs)


class ArticleDetail(View):
    def get(self, request, *args, **kwargs):
        view = ArticleDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ArticleComment.as_view()
        return view(request, *args, **kwargs)


class ArticleCreate(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = ("category", "title", "description", "image", "body", "draft")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleCreate, self).form_valid(form)


class ArticleUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = ("category", "title", "description", "image", "body", "draft")

    # Here we print out the name of the page updated
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.name)


class ArticleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Article
    success_url = reverse_lazy("articles:article_dashboard")

    # Here we overide the delete function to only work if a user is a superuser
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(author=self.request.user)
        return self.model.objects.all()


class ArticleCategory(generic.ListView):
    model = Article
    template_name = "articles/article_category.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Article.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(ArticleCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CategoryCreate(generic.CreateView):
    model = Category
    template_name = 'articles/category_form.html'
    fields = ('name',)

    def form_valid(self, form):
        form.instance = self.request.user
        form.save()
        return super(CategoryCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('articles:article_create')
