from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Article
from .forms import ArticleForm 
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:detail', article.pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): #매우중요
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    #article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    #article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    article.delete()
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    #article = Article.objects.get(pk=pk)
    
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        
        form = ArticleForm(request.POST, instance=article) #2번째 인자가 instance=article인 이유 : 없으면 create가 됨( 2줄 아래 save가 판단)
        if form.is_valid():
            form.save()
        return redirect('articles:detail', article.pk)
    #edit    
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)






