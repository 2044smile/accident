from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('content_1/', views.content_1, name='content_1'),
    path('content_2/', views.content_2, name='content_2'),
    path('content_3/', views.content_3, name='content_3'),
]