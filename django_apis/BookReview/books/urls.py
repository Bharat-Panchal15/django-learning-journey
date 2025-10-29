from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('reviews',ReviewViewSet, basename='review')

urlpatterns = router.urls