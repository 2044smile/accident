from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.photos, name='photos'),
    path('videos/', views.videos, name='videos'),

    path('content_1/', views.content_1, name='content_1'),
    path('content_2/', views.content_2, name='content_2'),
    path('content_3/', views.content_3, name='content_3'),
    path('content_4/', views.content_4, name='content_4'),
    path('content_5/', views.content_5, name='content_5')
]