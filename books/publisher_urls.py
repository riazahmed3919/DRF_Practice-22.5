from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewPublisherList.as_view(), name='publisher-list'),
    path('<int:pk>/', views.ViewPublisherDetails.as_view(), name='specific-publisher'),
]
