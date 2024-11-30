from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Comment
from .serializer import CommentSerializer

# Create your views here.
class CreateAndGetAllComments(ListCreateAPIView):
    queryset=Comment.objects.select_related('user','blog')
    serializer_class=CommentSerializer