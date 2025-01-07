from django.urls import path
from .views import news_list,source_list,news_detail, source_detail


urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('source/',source_list, name='source_list'),
    path('source/<int:pk>/', source_detail, name='source_detail')
]