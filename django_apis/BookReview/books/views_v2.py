from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSetV2(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['info'] = 'This is version 2 of the API.'
        return response