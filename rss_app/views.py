from django.shortcuts import render
from .models import Source, News
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SourceSerializer, NewsSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

language_param = openapi.Parameter(
    'language', openapi.IN_QUERY, description='Filter by language (en,ru,tm)', type=openapi.TYPE_STRING
)
search_param = openapi.Parameter(
    'search', openapi.IN_QUERY, description='Search', type=openapi.TYPE_STRING
)

order_param = openapi.Parameter(
    'order', openapi.IN_QUERY, description='Order_by => latest(pubDate), popular(view)', type=openapi.TYPE_STRING 
)

page_param = openapi.Parameter(
    'page', openapi.IN_QUERY, description='Page Number for pagination', type=openapi.TYPE_INTEGER
)

page_size_param = openapi.Parameter(
    'page_size', openapi.IN_QUERY, description='Number of items per page', type=openapi.TYPE_INTEGER
)

source_param = openapi.Parameter(
    'source', openapi.IN_QUERY, description='Filter by Source', type=openapi.TYPE_INTEGER
)

@swagger_auto_schema(
    method='get',
    manual_parameters=[language_param, search_param, order_param, page_param, page_size_param, source_param]
)
@api_view(['GET'])
def newsList(request):
    news = News.objects.all() 
    # Searching
    search_query = request.query_params.get('search', None)
    if search_query:
        news = news.filter(
            Q(title__icontains=search_query)|
            Q(summary__icontains=search_query)|
            Q(content__icontains=search_query),
        )

    # Orderin
    order = request.query_params.get('order', None)
    if order == 'latest':
        news = news.order_by('-pubDate')
    elif order == 'popular':
        news = news.order_by('-view')
    else:
        news = news.order_by('-pubDate')

    # Language
    language = request.query_params.get('language',None)
    if language:
        news = news.filter(source__language=language)

    # Source
    source = request.query_params.get('source', None)
    if source:
        news = news.filter(source=source)

    paginator = CustomPageNumberPagination()  # query param => page_size
    paginated_news = paginator.paginate_queryset(news, request)
    serializer = NewsSerializer(paginated_news, many=True,  context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def newsDetail(request,pk):
    new = News.objects.get(pk=pk)
    new.view +=1
    new.save()
    serializer = NewsSerializer(new, context={'request': request})

    return Response(
        serializer.data
    )


@swagger_auto_schema(
    method='get',
    manual_parameters=[language_param, search_param, page_param, page_size_param]
)
@api_view(['GET'])
def sourceList(request):
    source = Source.objects.all()
    # Searching
    search_query = request.query_params.get('search',None)
    if search_query:
        source = source.filter(
            Q(name__icontains=search_query)
        )

    # Language
    language = request.query_params.get('language', None)
    if language:
        source = source.filter(language=language)
    
    paginator = CustomPageNumberPagination()
    paginated_sources = paginator.paginate_queryset(source, request)
    serializer = SourceSerializer(paginated_sources, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def sourceDetail(request,pk):
    source = Source.objects.get(pk=pk)
    serializer = SourceSerializer(source, context={'request': request})
    return Response(
        serializer.data
    )
