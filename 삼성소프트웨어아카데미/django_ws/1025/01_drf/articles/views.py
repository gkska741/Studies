import rest_framework 
from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# Create your views here.


@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status= status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

