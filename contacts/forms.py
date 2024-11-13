from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']

class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100, required=False)
