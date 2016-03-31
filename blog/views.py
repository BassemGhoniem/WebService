from django.shortcuts import render

# Create your views here.


from rest_framework import generics, permissions


from .serializers import UserSerializer, PostSerializer
#from .models import User, Post, Photo

from.models import *

#         return queryset.filter(post__pk=self.kwargs.get('pk'))