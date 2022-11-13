from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def contact(request):
    return render(request, 'core/contact.html')
