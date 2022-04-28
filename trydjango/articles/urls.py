from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_view),
    path('articles/<slug:slug>/', views.article_detail_view, name= 'article-detail'),
    path('articles/new/create/', views.article_create_view, name='article-create'),
    path('articles/', views.article_search_view),
    
]