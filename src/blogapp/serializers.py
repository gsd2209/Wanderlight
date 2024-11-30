from rest_framework import serializers
from commentapp.models import Blog, Comment
from userapp.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'creator', 'comments']
        read_only_fields = ['id', 'creator']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the user from the request context
        
        # Create a new Blog instance, passing the creator user and validated data
        blog = Blog.objects.create(creator=user, **validated_data)
        
        return blog  # Return the created Blog instance
