from django.shortcuts import redirect, render
from .models import Article
# Create your views here.
def index(request):
    # 작성된 모든 게시글 출력

    articles = Article.objects.all() #QuerySet
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    #new로부터 title과 content를 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title = title, content = content)
    article.save()
        
    context = {
        'article': article
    }

    return render(request, 'articles/create.html', context)


def detail(request, pk):
    #all(), get(), filter()
    article = Article.objects.get(pk=pk) #(keyword = 실제pk값)
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
    pass


def delete(request, pk):
    
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index', article.pk)
    


def edit(request, pk):

    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
