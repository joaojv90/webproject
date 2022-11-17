from django.shortcuts import render
from portfolio.models import Portfolio
#from django.core.mail import EmailMessage
#from django.template.loader import render_to_string

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()[:6]
    return render(request, 'core/index.html', {'portfolios': portfolio})

def contact(request):
    return render(request, 'core/contact.html')
