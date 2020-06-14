"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path  
from .views import AuthorEdit, FriendEdit, FriendUpdate, FriendDelete, AuthorList, author_create_many, books_authors_create_many

app_name = 'p_library'  

urlpatterns = [
        path('author/create', AuthorEdit.as_view(), name='author_create'), # по .as_view() см. выше Class-based views
        path('authors', AuthorList.as_view(), name='author_list'),
        path('author/create_many', author_create_many, name='author_create_many'),
        path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
        path('friend/create', FriendEdit.as_view()),
        path('friends/<int:pk>/', FriendUpdate.as_view()),
        path('friends/<int:pk>/delete/', FriendDelete.as_view()),
]
  