from django.urls import path
from books import views

urlpatterns = [
    path('', views.view_authors, name='author-list'),
    path('<int:pk>/', views.view_specific_author, name='specific-author'),
]
