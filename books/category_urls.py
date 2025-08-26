from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewCategoryList.as_view(), name='category-list'),
    path('<int:pk>/', views.ViewCategoryDetails.as_view(), name='specific-category'),
]
