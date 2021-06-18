from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('$/', views.posts, name='posts'),
    # path('$/', views.comments, name='comments'),
    path('post/', views.individual_post, name='individual_post'),
]