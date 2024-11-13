from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm, SearchForm
from django.conf import settings

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send email
            recipient = request.POST.get('recipient_email')
            if recipient:
                send_mail(
                    'New Contact Added',
                    f'Contact Details:\nName: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}',
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient],
                )
            return redirect('view_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def view_contacts(request):
    form = SearchForm(request.GET or None)
    contacts = Contact.objects.all()
    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        contacts = contacts.filter(name__icontains=query) | contacts.filter(email__icontains=query)
    return render(request, 'contacts/view_contacts.html', {'contacts': contacts, 'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('view_contacts')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})
