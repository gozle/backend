from django.urls import path
from .views import newsList,sourceList,newsDetail


urlpatterns = [
    path('newsList/', newsList, name='newsList'),
    path('sourceList/',sourceList, name='sourceList'),
    path('newsDetail/<int:pk>/', newsDetail, name='newsDetail')
]