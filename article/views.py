from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .models import Article

CATEGORY_MAPPING = {
    'eco': 'economie',
    'politique': 'politique',
    'finances': 'finances',
    'societe': 'societes',
    'entreprise': 'entreprise',
    'international': 'international'
}


class ArticlesByCategoryView(TemplateView):
    template_name = 'index/politiques/politique.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_name = self.kwargs.get('category_name')
        actual_category_name = CATEGORY_MAPPING.get(category_name, category_name)

        context['unes'] = Article.objects.filter(alerte_info=True)
        context['is_special'] = Article.objects.filter(is_special=True)
        context['published_articles'] = Article.objects.filter(category__name=actual_category_name, status='Published')[:3]

        return context


class DetailArticleView(DetailView):
    model = Article
    template_name = 'index/politiques/detail.html'
    context_object_name = 'get_detail_article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unes'] = Article.objects.filter(alerte_info=True)
        context['is_special'] = Article.objects.filter(is_special=True)
        context['published_articles'] = Article.objects.filter(status='Published')[:3]
        return context
