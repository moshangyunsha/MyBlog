from django.shortcuts import render

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by('-create_time')

    serializer_class = PostSerializer

# Create your views here.
