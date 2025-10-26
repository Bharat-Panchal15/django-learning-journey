from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import BookListAPIView, BookDetailAPIView
from .views import BookViewSet

# urlpatterns = [
#     path('books/',BookListAPIView.as_view(),name='book-list'),
#     path('book/<int:pk>',BookDetailAPIView.as_view(), name='book-detail'),
# ]

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = router.urls