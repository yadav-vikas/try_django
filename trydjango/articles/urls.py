from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_view),
    path('articles/<int:id>/', views.article_detail_view),
    path('articles/create/', views.article_create_view),
    path('articles/', views.article_search_view),
    
]