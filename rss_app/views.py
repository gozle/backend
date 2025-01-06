from django.shortcuts import render
from .models import Source, News
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SourceSerializer, NewsSerializer

@api_view(['GET'])
def newsList(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)

    return Response(
        serializer.data,
    )


@api_view(['GET'])
def newsDetail(request,pk):
    new = News.objects.get(pk=pk)
    serializer = NewsSerializer(new)

    return Response(
        serializer.data
    )

@api_view(['GET'])
def sourceList(request):
    source = Source.objects.all()
    serializer = SourceSerializer(source, many=True)

    return Response(
        serializer.data
    )