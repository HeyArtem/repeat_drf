from django.shortcuts import render
from rest_framework import serializers, status
from .models import BlogPost, BlogPostCategory
from blog_app.api.serializers import BlogPostSerializer, BlogPostCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


# указываем какие методы будем использовать
@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        blog_posts = BlogPost.objects.filter(status='published')
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail(request, pk):
    
    # в случае ошибки (ВЫЗОВА НЕ СУЩЕСТВУЮЩЕГО ПОСТА) работа сервера на завершается, а будет ошибка 404
    blog_post = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == 'GET':
        # blog_post = BlogPost.objects.get(pk=pk)       
        
        # альтернативное написание (вручную)(ВЫЗОВА НЕ СУЩЕСТВУЮЩЕГО ПОСТА)
        # try:
        #     blog_post = BlogPost.objects.get(pk=pk)
        # except Exception as ex:
        #     return Response(
        #         {
        #             'error': {
        #                 'code': 404,
        #                 'message': 'Pooost is noot fooouuund!'
        #             }
        #         }
        #     )
        
        # еще альтернатива        
        # try:
        #     blog_post = BlogPost.objects.get(pk=pk)
        # except BlogPost.DoesNotExist:
        #     return Response(
        #         {
        #             'error': {
        #                 'code': 404,
        #                 'message': 'Pooost is noot fooouuund!'
        #             }
        #         }
        #     )
        
        
        
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        
        serializer = BlogPostSerializer(blog_post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        blog_post.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# get, put, delete
# just test commit
