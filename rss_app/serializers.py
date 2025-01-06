from rest_framework import serializers
from .models import Source, News

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['name', 'link', 'language', 'icon']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['source', 'title', 'summary' ,'content', 'photo', 'url', 'view','pubDate','created_at']