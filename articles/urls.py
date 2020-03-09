# from django.conf.urls import url
from django.urls import path
# from django.views.generic import FormView
from articles import views

# from .forms import ArticleForm

urlpatterns = [
    # url(r'^category/(?P<pk>[\w-]+)/$', views.ArticleCategory.as_view(), name='article_category'),
    # url(r'^delete/(?P<slug>[\w-]+)/$', views.ArticleDelete.as_view(), name='article_delete'),
    # url(r'^update/(?P<slug>[\w-]+)/$', views.ArticleUpdate.as_view(), name='article_update'),
    # url(r'^dashboard/$', views.DashBoard.as_view(), name='article_dashboard'),
    # url(r'^create/$', views.ArticleCreate.as_view(), name='article_create'),
    # url(r'^details/(?P<slug>[\w-]+)$', views.ArticleDetail.as_view(), name='article_detail'),
    # url(r'^$', views.ArticleList.as_view(), name='article_list'),
    path('category/create', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>', views.ArticleCategory.as_view(), name='article_category'),
    path('delete/<slug:slug>', views.ArticleDelete.as_view(), name='article_delete'),
    path('update/<slug:slug>', views.ArticleUpdate.as_view(), name='article_update'),
    path('dashboard/', views.DashBoard.as_view(), name='article_dashboard'),
    path('create/', views.ArticleCreate.as_view(), name='article_create'),
    path('details/<slug:slug>', views.ArticleDetail.as_view(), name='article_detail'),
    path('', views.ArticleList.as_view(), name='article_list'),
]
