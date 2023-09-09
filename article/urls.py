from django.urls import path

from . import views
from .views import ArticlesByCategoryView, DetailArticleView

app_name = 'articles'
urlpatterns = [
    path('politique/', ArticlesByCategoryView.as_view(), {'category_name': 'politique'}, name='politiques'),
    path('economie/', ArticlesByCategoryView.as_view(), {'category_name': 'eco'}, name='eco'),
    path('finances/', ArticlesByCategoryView.as_view(), {'category_name': 'finances'}, name='articlefinance'),
    path('societe/', ArticlesByCategoryView.as_view(), {'category_name': 'societe'}, name='articlesociete'),
    path('innovation/', ArticlesByCategoryView.as_view(), {'category_name': 'entreprise'}, name='entreprise'),
    path('international/', ArticlesByCategoryView.as_view(), {'category_name': 'international'}, name='internation'),
    path('<slug:slug>/', DetailArticleView.as_view(), name='detail_view')

]
