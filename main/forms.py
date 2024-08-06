from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, min_length=3)
    email = forms.EmailField(required=True, max_length=150, min_length=5)
    location = forms.ChoiceField(choices=[('Wrocław', 'Wrocław'), ('Brzeg', 'Brzeg'), ('Wieruszów', 'Wieruszów')], required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data