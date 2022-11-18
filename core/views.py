from django.shortcuts import render, redirect
from portfolio.models import Portfolio
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()[:6]
    return render(request, 'core/index.html', {'portfolios': portfolio})

def contact(request):
    if request.method == "POST":
        name = request.post['name']
        email = request.post['email']
        message = request.post['message']

        template = render_to_string('email_template.html',{
            'name':name,
            'email':email,
            'message': message})

        email = EmailMessage(
            template,
            settings.EMAIL_HOST_USER,
            ['cybertools.tech@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request,'Su mensaje a sido enviado.')

        return redirect('core/contact.html')

    return render(request, 'core/contact.html')
