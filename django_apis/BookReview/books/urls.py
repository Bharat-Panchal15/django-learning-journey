from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListAPIView, BookDetailAPIView
from .views import BookViewSet, SecretAPIView

urlpatterns = [
    path('books/',BookListAPIView.as_view(),name='book-list'),
    path('book/<int:pk>',BookDetailAPIView.as_view(), name='book-detail'),
]

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('secret/',SecretAPIView.as_view(), name='secret'),
]
urlpatterns += router.urls