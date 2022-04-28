from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','Timestamp','updated','slug']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
