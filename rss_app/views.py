from django.shortcuts import render
from .models import Source, News
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SourceSerializer, NewsSerializer
from .pagination import CustomPageNumberPagination

@api_view(['GET'])
def newsList(request):
    news = News.objects.order_by('-pubDate')
    popular_news = News.objects.order_by('-view')
    latest_news = News.objects.order_by('-pubDate')  # pubDate

    paginator = CustomPageNumberPagination()  # query param => page_size

    paginated_news = paginator.paginate_queryset(news, request)
    paginated_popular_news = paginator.paginate_queryset(popular_news, request)
    paginated_latest_news = paginator.paginate_queryset(latest_news, request)

    serializer = NewsSerializer(paginated_news, many=True)
    popular_news_serializer = NewsSerializer(paginated_popular_news, many=True)
    latest_news_serializer = NewsSerializer(paginated_latest_news, many=True)

    return Response({
        "news":serializer.data,
        'popular_news':popular_news_serializer.data,
        "latest_news":latest_news_serializer.data
    })
    # return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def newsDetail(request,pk):
    new = News.objects.get(pk=pk)
    new.view +=1
    new.save()
    serializer = NewsSerializer(new)

    return Response(
        serializer.data
    )

@api_view(['GET'])
def sourceList(request):
    source = Source.objects.all()
    paginator = CustomPageNumberPagination()
    paginated_sources = paginator.paginate_queryset(source, request)

    serializer = SourceSerializer(paginated_sources, many=True)

    return Response(
        serializer.data
    )