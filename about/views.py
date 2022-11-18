from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):  
    about = About.objects.all()  # select
    return render(request, 'about/about.html', {'abouts': about})
