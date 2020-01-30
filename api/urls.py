from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, BookAuthorViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)
router.register('author', AuthorViewSet)
router.register('book-author', BookAuthorViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
