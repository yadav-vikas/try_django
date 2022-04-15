from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import random
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import  ArticleFormold, ArticleForm

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object" : article_obj,
    }
    return render(request, "articles/detail.html", context=context)

def article_view(request):
    context = {
        'posts' : Article.objects.all()
    }
    return render(request, "home-view.html", context=context)


def article_search_view(request):
    query_dict = request.GET # dictionary
    # query = query_dict.get("q")
    try:
        query = int(query_dict.get("q"))
    except :
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object" : article_obj
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):  
    form = ArticleForm(request.POST or None)      
    context = {
        "form" : ArticleForm()
    }
    # if request.method == "POST":
    #     form = ArticleForm(request.POST)
    context['form'] = form
    if form.is_valid():
        obj = form.save()
        context['form'] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # # print(title, content)
        # article_object = Article.objects.create(title=title, content=content)
        # context['object'] = article_object
        # context['created'] = True
    
    return render(request, "articles/create.html", context=context)
