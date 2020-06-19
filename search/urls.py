from django.urls import path
from . import views


app_name = 'archive'

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
]