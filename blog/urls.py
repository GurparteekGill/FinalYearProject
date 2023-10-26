from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost")
 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

