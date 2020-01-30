from rest_framework import serializers
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname')

class BookAuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ('title', 'description', 'author')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        extra_kwarg = { 'password': { 'write_only': True, 'required': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        token = Token.objects.create(user=user)
        return user
