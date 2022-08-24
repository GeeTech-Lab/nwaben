from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'burial_memories'

urlpatterns = [
    path("", views.BurialMemoryList.as_view(), name='list'),
    path('create/', views.BurialMemoryCreate.as_view(), name='create'),
    path("<slug:slug>/", views.BurialMemoryDetail.as_view(), name='detail'),
    path('update/<slug:slug>', views.BurialMemoryUpdate.as_view(), name='update'),
    path('delete/<slug:slug>', views.BurialMemoryDelete.as_view(), name='delete'),
]

htmx_urlpatterns = [
    path('<slug:slug>/tribute/', views.add_tribute, name='add_tribute'),
    path('<slug:slug>/donate/', csrf_exempt(views.add_donation), name='add_donation'),
    path('<slug:slug>/donation_list/', views.list_donations, name='list_donations'),
    path('gallery_list/<slug:slug>/', views.list_gallery, name='list_gallery'),
]

urlpatterns += htmx_urlpatterns
