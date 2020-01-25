from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from articles import models


class ArticleList(ListView):
    template_name = "article_list"
    model = models.Article

class ArticleDetail(LoginRequiredMixin, DetailView):
    template_name = "article_detail"
    models = models.Article