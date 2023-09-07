from django.shortcuts import render
from article.models import Article
from .forms import SearchForm


def home(request):
    published_articles_vogues = Article.objects.filter(is_featured=True, status='Published', en_vedette=False)[:1]
    published_articles = Article.objects.filter(status='Published', en_vedette=True, is_featured=False)[:3]
    politiques = Article.objects.filter(category__name="politique", status='Published')[:6]
    economies = Article.objects.filter(category__name="economie", status='Published')[:6]
    finances = Article.objects.filter(category__name="finances", status='Published')[:6]
    societes = Article.objects.filter(category__name="societes", status='Published')[:6]
    entreprises = Article.objects.filter(category__name="entreprise", status='Published')[:6]
    internationales = Article.objects.filter(category__name="international", status='Published')[:6]
    is_special = Article.objects.filter(is_special=True),
    unes = Article.objects.filter(alerte_info=True)

    contexte = {
        "published_articles": published_articles,
        "published_articles_vogues": published_articles_vogues,
        "politiques": politiques,
        "economies": economies,
        "finances": finances,
        "societes": societes,
        "entreprises": entreprises,
        "internationales": internationales,
        'is_special': is_special,
        "unes": unes

    }
    return render(request, 'home/home.html', contexte)


def rechercher(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            result = Article.objects.filter(title__icontains=search)

            if result.exists():
                return render(request, 'base.html')
            else:
                message = 'Aucun résultat trouvé pour votre recherche '
                return render(request, 'base.html', {'form': form, 'message': message})
        else:
            form = SearchForm()
            return render(request, 'base.html', {'form': form})

    return render(request, 'base.html')
