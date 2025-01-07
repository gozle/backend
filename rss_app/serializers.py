from rest_framework import serializers
from .models import Source, News


class SourceSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    class Meta:
        model = Source
        fields = ['id','name', 'link', 'language', 'icon']

    def get_icon(self, source):
        request = self.context.get('request')
        if source.icon:
            icon_url = source.icon.url
            return request.build_absolute_uri(icon_url)
        return None


class NewsSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    photo = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['id','source', 'title', 'summary' ,'content', 'photo', 'url', 'view','pubDate','created_at']
    
    def get_photo(self, news):
        request = self.context.get('request')
        if news.photo:
            photo_url = news.photo.url
            return request.build_absolute_uri(photo_url)


