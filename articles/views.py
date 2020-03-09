from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from .forms import ArticleForm, CommentForm, CategoryForm
from .models import Category, Article, Comment


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
        object = super(ArticleDisplay, self).get_object()
        object.view_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(ArticleDisplay, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.get_object())
        context['form'] = CommentForm
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
    success_url = reverse_lazy("article_dashboard")

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