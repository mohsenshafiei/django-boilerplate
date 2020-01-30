from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import BookAuthorSerializer
from .serializers import UserSerializer
from .models import Book, Author
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def first(request):
    return HttpResponse('first message from views')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer;
    queryset = Book.objects.all();
    authentication_classes = (TokenAuthentication,);
    permission_classes = (IsAuthenticated,);

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer;
    queryset = Author.objects.all();
    authentication_classes = (TokenAuthentication,);
    permission_classes = (IsAuthenticated,);

class BookAuthorViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer;
    queryset = Book.objects.all();
    authentication_classes = (TokenAuthentication,);
    permission_classes = (IsAuthenticated,);

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = BookAuthorSerializer(instance)
        return Response(serializers.data)
