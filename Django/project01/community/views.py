from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .models import SampleModel
from .forms import SampleModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    forms = SampleModel.objects.order_by('pk')
    context = {
        'forms': forms,
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST': # 받은 정보를 렌더링해서 create한다
        form = SampleModelForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('community:detail', article.pk)
    else: # 기본 폼을 보낸다
        form = SampleModelForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)

@require_safe
def detail(request, pk):
    article = get_object_or_404(SampleModel, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_POST
def delete(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(SampleModel, pk=pk)
        article.delete()
    return redirect('community:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(SampleModel, pk=pk)
    if request.method == 'POST':
        form = SampleModelForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('community:detail', article.pk)
    else:
        form = SampleModelForm(instance=article)
    context= {
        'article': article,
        'form': form,
    }
    return render(request, 'community/update.html', context)


    

