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
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from nwaben.views import ContactView



urlpatterns = [
    path('admin', admin.site.urls),
    path('page-not-found/', TemplateView.as_view(template_name='404_.html'), name='404_'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', ContactView.as_view(), name='about'),
    path('api/auth/', include(('accounts.api.urls', 'api-auth'), namespace='api-auth')),
    path('account/', include(('accounts.urls', 'account-url'), namespace='account-url')),
    path('api/auth/', include(('accounts.api.urls', 'api-auth'), namespace='api-auth')),
]


urlpatterns += staticfiles_urlpatterns()
# Remove this conditional check if you want to upload to Heroku
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)