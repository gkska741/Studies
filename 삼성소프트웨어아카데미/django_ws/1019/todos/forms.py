from django import forms
from .models import Todo

class TodoForm(forms.Modelform):
    class meta:
        model = Todo
        exclude = ('author')

