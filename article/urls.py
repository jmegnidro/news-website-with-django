from django.urls import path
from .views import index, detail, eco, ecodetail, finaces, finacesdetail, societe, societesdetail, entreprisedetail, \
    entreprise, intenationaldetail, international

app_name = 'articles'
urlpatterns = [
    path('politique', index, name='politiques'),
    path('politique/<str:slug>/', detail, name='detail'),
    # economie
    path('economie/', eco, name='eco'),
    path('economie/<slug:slug>/', ecodetail, name='eco-article'),
    # finances
    path('finances/', finaces, name='articlefinance'),
    path('finances/<slug:slug>/', finacesdetail, name='articlefinance'),
    # societe
    path('societe/', societe, name='articlesociete'),
    path('societe/<slug:slug>/', societesdetail, name='articledetailsociete'),
    # entreprise
    path('innovation/', entreprise, name='entreprise'),
    path('innovation/<slug:slug>/', entreprisedetail, name='entreprisedetail'),

    # international
    path('international/', international, name='internation'),
    path('international/<slug:slug>/', intenationaldetail, name='internationdetail'),

]
