"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include 
from books import views as books_views

urlpatterns = [
    path("", books_views.list_books, name="list_books"),
    path("admin/", admin.site.urls),
    path('books/add_book/', books_views.add_book, name='add_book'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/<int:pk>/add_favorite', books_views.add_favorite, name='add_favorite'),
    path('books/<int:pk>/remove_favorite', books_views.remove_favorite, name='remove_favorite'),
]
