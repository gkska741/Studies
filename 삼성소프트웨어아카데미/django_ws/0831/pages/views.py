from django.shortcuts import render

# Create your views here.
def dinner(request, menu, numbers):
    context = {
        'menu': menu,
        'numbers': numbers,
    }

    return render(request, 'dinner.html', context)