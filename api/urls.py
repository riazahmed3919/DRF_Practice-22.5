from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, CategoryViewSet, AuthorViewSet, PublisherViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]