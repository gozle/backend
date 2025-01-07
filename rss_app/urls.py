from django.urls import path
from .views import newsList,sourceList,newsDetail, sourceDetail


urlpatterns = [
    path('news/', newsList, name='newsList'),
    path('news/<int:pk>/', newsDetail, name='newsDetail'),
    path('source/',sourceList, name='sourceList'),
    path('source/<int:pk>/', sourceDetail, name='sourceDetail')
]