from rest_framework import serializers
from .models import Comment
from blogapp.serializers import UserSerializer,BlogSerializer
from blogapp.models import Blog



class CommentSerializer(serializers.ModelSerializer):
    blog_id=serializers.IntegerField(write_only=True)
    blog_id=BlogSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model=Blog
        fields=['id','title','description','image','creator']
        read_only_fields=['id','created_at','user','blog']

    def create(self,validate_data):
        user = self.context['request'].user

        blog_id=validate_data.pop('blog_id')
        try:
            blog=Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            raise serializers.ValidationError({'blog_id':'Blog does not exist'})

        
        return Comment.objects.create(user=user,blog=blog,**validate_data) 