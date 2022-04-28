from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
import random
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import  ArticleFormold, ArticleForm
from django.http import  Http404
from django.db.models import Q

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)

def article_view(request):
    context = {
        'posts' : Article.objects.all()
    }
    return render(request, "home-view.html", context=context)


def article_search_view(request):
    query = request.GET.get('q') # dictionary
    # query = query_dict.get("q")
    # qs = Article.objects.all()
    # article_obj = None
    # if query is not None:
    #     # lookups = Q(title__icontains=query) | Q(content__icontains=query)
    #     # qs = Article.objects.filter(lookups)
    #     qs = Article.objects.search(query)

    qs = Article.objects.search(query=query)
    context = {
        "object_list" : qs
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):  
    form = ArticleForm(request.POST or None)      
    context = {
        "form" : form
    }
    # if request.method == "POST":
    #     form = ArticleForm(request.POST)
    context['form'] = form
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # return redirect("article-detail", slug=article_object.slug)
        return redirect(article_object.get_absolute_url())
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # # print(title, content)
        # article_object = Article.objects.create(title=title, content=content)
        # context['object'] = article_object
        # context['created'] = True
    
    return render(request, "articles/create.html", context=context)
