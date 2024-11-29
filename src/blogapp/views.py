from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Blog
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import PermissionDenied

# Create your views here.

# class CreateAndGetAllBlogs(APIView):
#     def get(self, request):
#         blogs = Blog.objects.all().values()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response({'blogs': serializer.data})
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Blog created successfully', 'blog': serializer.data}, status=201)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GetUpdateDeleteBlog(APIView):
#     def getBlog(self, id):
#         try:
#             return Blog.objects.get(id=id)
#         except Blog.DoesNotExist:
#             return None
        
#     def get(self, request, id):
#         blog = self.getBlog(id)
#         if blog is None:
#             return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BlogSerializer(blog)
#         return Response({'blog': serializer.data})
    
#     def put(self, request, id):
#         blog = self.getBlog(id)
#         if blog is None:
#             return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BlogSerializer(blog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Blog updated successfully', 'blog': serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         blog = self.getBlog(id)
#         if blog is None:
#             return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
#         blog.delete()
#         return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CreateAndGetAllBlogs(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filter_backends = [OrderingFilter]
    ordering_fields =['title','id','update_at','create_at']
    ordering =['id']

class GetUpdateDeleteBlog(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

    def perform_update(self,serializer):
        blog=self.get_object()
        if blog.creator != self.request.user:
            raise PermissionDenied('you do not have permsision to update this blog')
        old_image = blog.image

        updated_blog = serializer.save()

        if old_image and old_image != updated_blog.image:
            print(f'deleting old image: {old_image.name}')
            old_image.delete(save=False)
        else:
            print('no image chnage detected or no old image to delete')

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionDenied('you do not have permsision to delete this blog')
        if instance.image:
            instance.image.delete(save=False)
        instance.delete()

class GetUserBlogs(ListAPIView):
    serializer_class=BlogSerializer
    def get_queryset(self):
            return Blog.objects.filter(creator=self.request.user)