from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet
from .views_v2 import BookViewSetV2

router_v1 = DefaultRouter()
router_v1.register('books', BookViewSet, basename='book')
router_v1.register('reviews', ReviewViewSet, basename='review')

router_v2 = DefaultRouter()
router_v2.register('books', BookViewSetV2, basename='book-v2')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v2/', include(router_v2.urls)),
]