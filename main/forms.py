from django import forms 

class ShippingForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Imię')
    last_name = forms.CharField(max_length=100, label='Nazwisko')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(max_length=15, label='Numer telefonu')
    address = forms.CharField(max_length=255, label='Adres')
    postal_code = forms.CharField(max_length=10, label='Kod pocztowy')
    city = forms.CharField(max_length=100, label='Miejscowość')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.startswith('+48'):
            raise forms.ValidationError('Numer telefonu musi zaczynać się od +48')
        return phone