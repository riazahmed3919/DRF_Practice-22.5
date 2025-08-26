from django.urls import path
from books import views

urlpatterns = [
    path('', views.view_publishers, name='publisher-list'),
    path('<int:pk>/', views.view_specific_publisher, name='specific-publisher'),
]
