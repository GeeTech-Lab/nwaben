from django.shortcuts import render
from django.views.generic import ListView


class SearchView(ListView):
    model = Album
