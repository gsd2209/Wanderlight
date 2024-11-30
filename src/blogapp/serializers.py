from rest_framework import serializers
from .models import Blog
from userapp.serializers import UserSerializer



class BlogSerializer(serializers.ModelSerializer):
    creator= UserSerializer(read_only=True)
    class Meta:
        model=Blog
        fields=['id','title','description','image','creator']
        read_only_fields=['id','creator']

    def create(self,validate_data):
        user = self.context['request'].user

        blog= Blog.objects.create(creator=user,**validate_data)
        return Blog