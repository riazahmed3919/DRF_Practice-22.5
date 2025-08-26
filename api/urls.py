from django.urls import path, include
from rest_framework_nested import routers
from books.views import BookViewSet, CategoryViewSet, AuthorViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]