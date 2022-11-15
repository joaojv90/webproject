from django.shortcuts import render
from .models import About

# Create your views here.


def about(request):  # Esta solo es el nombre de la vista
    about = About.objects.all()  # select
    return render(request, 'about/about.html', {'abouts': about})
