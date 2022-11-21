from django.shortcuts import render, redirect
from portfolio.models import Portfolio
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()[:6]
    return render(request, 'core/index.html', {'portfolios': portfolio})

def contact(request):
    contactForm = ContactForm()
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        email = EmailMessage(
            "Cybertools : Nuevo mensaje de contacto",
            "De {} <{}>\n\nEscribir:\n\n{}".format(name, email, message),
            "no-contestar@inbox.mailtrap.io",
            ["jojaramillo@itsqmet.edu.ec"],
            reply_to=[email]
        )

        # Enviar mail
        try:
            email.send()
            return redirect(reverse('contact') + '?ok')
        except:
            return redirect(reverse('contact') + '?fail')

    return render(request, 'core/contact.html', {'contactForm': contactForm})
