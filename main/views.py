from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def form1(request):
    return render(request, 'main/form1.html')

def form2(request):
    return render(request, 'main/form2.html')

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'location': form.cleaned_data['location'],
                'message': form.cleaned_data['message'],
            }

            #Send email
            html_body = render_to_string('email_templates/appointment.html', data)

            msg = EmailMultiAlternatives(
                subject='Appointment',
                body=html_body,
                from_email = data['email'],
                to=['pavlokiht2005@gmail.com'],
                reply_to=[data['email']])
                
            msg.attach_alternative(html_body, "text/html")
            msg.send()

            #return JsonResponse(data)
            return JsonResponse({'success': data})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('index')

