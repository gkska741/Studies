# Workshop Problem_0831


```python
#intro/urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<menu>/<numbers>/', views.dinner)
```


```python
#pages/views.py

from django.shortcuts import render

# Create your views here.
def dinner(request, menu, numbers):
    context = {
        'menu': menu,
        'numbers': numbers,
    }

    return render(request, 'dinner.html', context)
```


```python
#templates/dinner.html

<h1> 저녁 메뉴</h1>
<h1> 저녁 먹을 사람?! {{numbers}}</h1>
<h1> 어떤 메뉴?! {{menu}}</h1>

```
