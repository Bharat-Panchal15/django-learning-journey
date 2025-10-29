from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id','book','user','rating','comment','created_at']
        read_only_fields = ['id','user','created_at']

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'