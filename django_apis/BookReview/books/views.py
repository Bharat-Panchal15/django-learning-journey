from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework.backends import DjangoFilterBackend
from .models import Book, Review
from .permissions import IsOwnerOrReadOnly 
from .serializers import BookSerializer, ReviewSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['author']
    ordering_fields = ['published_date']
    search_fields = ['title','author']

    def list(self, request, *args, **kwargs):
        current_version = request.version
        print(f"API version in use: {current_version}")
        return super().list(request, *args, **kwargs)
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['book','rating','user'] # =?book1 or %rating=5
    ordering_fields = ['rating','created_at']
    search_fields = ['comment']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)