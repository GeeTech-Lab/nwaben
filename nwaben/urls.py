"""nwaben URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from nwaben.views import ContactView

urlpatterns = [
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('burial_memories/', include('burial_memories.urls', namespace='burial_memories')),
    path('about/', ContactView.as_view(), name='about'),
    path('articles/', include(('articles.urls', 'articles'), namespace='articles')),
    # path('archives/', include('archive.urls', namespace='archives')),
    path('mp3/', include('mp3.urls', namespace='mp3')),
    path('search/', include('search.urls', namespace='search')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('summernote/', include('django_summernote.urls')),
]

# urlpatterns += staticfiles_urlpatterns()
# # Remove this conditional check if you want to upload to Heroku
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# administrator backend service url
urlpatterns += [
    path('admin-family-nwaben/', admin.site.urls),
]

# Url to catch any un-matched pattern and render 404
urlpatterns += [re_path(r'^.*.', TemplateView.as_view(template_name='404.html'), name='404_')]
