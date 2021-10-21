from django.db.models import fields
from rest_framework import serializers
# два варианат импортирования моделей
# from ..models import BlogPost, BlogPostCategory
from blog_app.models import BlogPost, BlogPostCategory
from rest_framework import status


class BlogPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostCategory
        fields = '__all__'
        # exclude = ("id", )


class BlogPostSerializer(serializers.ModelSerializer):    
    # category = BlogPostCategorySerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'
        

        
        

