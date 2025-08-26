from django.urls import path
from books import views

urlpatterns = [
    path('', views.view_categories, name='category-list'),
    path('<int:pk>/', views.view_specific_category, name='specific-category'),
]
