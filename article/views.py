from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.


def index(request):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="politique", status='Published')

    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes,

    }
    return render(request, 'index/politiques/politique.html', contexte)


def detail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="politique", status='Published')[:3]
    get_detai_article = get_object_or_404(Article, slug=slug)
    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/politiques/detail.html', contexte)


def eco(request):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="economie", status='Published')
    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/economie/politique.html', contexte)


def ecodetail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="economie", status='Published')[:3]
    get_detai_article = Article.objects.get(slug=slug)
    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/economie/detail.html', contexte)


def finaces(request):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="finances", status='Published')
    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/finances/politique.html', contexte)


def finacesdetail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="finances", status='Published')[:3]
    get_detai_article = Article.objects.get(slug=slug)
    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/finances/detail.html', contexte)


# societé

def societe(request):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="societes", status='Published')
    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/societe/politique.html', contexte)


def societesdetail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    published_articles = Article.objects.filter(category__name="societes", status='Published')[:3]
    get_detai_article = Article.objects.get(slug=slug)
    is_special = Article.objects.filter(is_special=True)

    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/societe/detail.html', contexte)


def entreprise(request):
    unes = Article.objects.filter(alerte_info=True)
    is_special = Article.objects.filter(is_special=True)
    published_articles = Article.objects.filter(category__name="entreprise", status='Published')
    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/entreprise/politique.html', contexte)


def entreprisedetail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    published_articles = Article.objects.filter(category__name="entreprise", status='Published')[:3]
    get_detai_article = Article.objects.get(slug=slug)
    is_special = Article.objects.filter(is_special=True)

    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/entreprise/detail.html', contexte)


def international(request):
    is_special = Article.objects.filter(is_special=True)
    unes = Article.objects.filter(alerte_info=True)

    published_articles = Article.objects.filter(category__name="international", status='Published')
    contexte = {
        'published_articles': published_articles,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/international/politique.html', contexte)


def intenationaldetail(request, slug):
    unes = Article.objects.filter(alerte_info=True)
    published_articles = Article.objects.filter(category__name="international", status='Published')[:3]
    get_detai_article = Article.objects.get(slug=slug)
    is_special = Article.objects.filter(is_special=True)

    contexte = {
        'published_articles': published_articles,
        'get_detai_article': get_detai_article,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'index/international/detail.html', contexte)
