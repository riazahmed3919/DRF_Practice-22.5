from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewPublishers.as_view(), name='publisher-list'),
    path('<int:pk>/', views.ViewSpecificPublishers.as_view(), name='specific-publisher'),
]
