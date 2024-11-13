from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse

from .models import contactus


def home(request):
    return HttpResponse("This is klu project with CSE app")
def base(request):
    return render(request,'base.html')
def login(request):
    return render(request,'login1.html')
# Create your views here.
def logout(request):
    return render(request,'logout.html')


from .forms import LocationForm
from datetime import datetime
import pytz
def timezonepagecall(request):
    return render(request,'timezonepage.html')

def timezonepagelogic(request):
    current_time = None
    selected_location = None
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            selected_location = form.cleaned_data['timezone']
            timezone = pytz.timezone(selected_location)
            current_time = datetime.now(timezone)
            print(f"Selected Location: {selected_location}")
            print(f"Current Time: {current_time}")
    else:
        form = LocationForm()

    context = {
        'form': form,
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S') if current_time else None,
        'selected_location': selected_location,
    }
    print("Context Data:", context)
    return render(request, 'timezonepage.html', context)


def contactpagecall(request):
    return render(request, 'contact.html')


def contactlogic(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        subject = 'Thank You for ur valuable Feedback'
        send_mail(
            subject,
            comment,
            'gkarthik8461@gmail.com',  # Update with your sender email
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Thank you for giving Feedback </center></h1>")
    else:
        HttpResponse("<h1>error</h1>")