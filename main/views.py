from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import ShippingForm


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def form1(request):
    return render(request, 'main/form1.html')

def form2(request):
    return render(request, 'main/form2.html')

def shipping_view(request):
    # Sprawdzenie, czy metoda żądania to POST
    if request.method == 'POST':
        # Tworzenie instancji formularza z danymi z POST
        form = ShippingForm(request.POST)
        
        # Sprawdzanie, czy formularz jest poprawny
        if form.is_valid():
            # Pobieranie danych z formularza
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            postal_code = form.cleaned_data['postal_code']
            city = form.cleaned_data['city']
            
            # Wysyłanie e-maila z potwierdzeniem zamówienia
            send_mail(
                'Potwierdzenie zamówienia', 
                f'Witaj {first_name} {last_name},\n\nTwoje zamówienie zostało złożone pomyślnie. Dziękujemy za zakupy w naszym sklepie.', 
                settings.EMAIL_HOST_USER, 
                [email]
            )
            
            # Przekierowanie użytkownika na stronę sukcesu
            return redirect("success")
    else:
        # Tworzenie pustej instancji formularza
        form = ShippingForm()
    
    # Renderowanie szablonu z formularzem
    return render(request, 'main/shipping.html', {'form': form})
