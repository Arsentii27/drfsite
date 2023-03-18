from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Superheroes, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import SuperheroesSerializer

class SuperheroesAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2

class SuperheroesAPIList(generics.ListCreateAPIView):
    queryset = Superheroes.objects.all()
    serializer_class = SuperheroesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = SuperheroesAPIListPagination

class SuperheroesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Superheroes.objects.all()
    serializer_class = SuperheroesSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class SuperheroesAPIDestroy(generics.RetrieveUpdateAPIView):
    queryset = Superheroes.objects.all()
    serializer_class = SuperheroesSerializer
    permission_classes = (IsAdminOrReadOnly, )