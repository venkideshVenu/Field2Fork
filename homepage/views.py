from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_home_page(request):
    return render(request, 'temp_homepage/home.html',context={})

def get_about_page(request):
    return render(request, 'temp_homepage/about.html',context={})



def get_error_page(request):
    return render(request, 'temp_homepage/404.html',context={})



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages

def get_contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            try:
                send_mail(
                    f'Contact Form Submission: {subject}',
                    f'Name: {name}\nEmail: {email}\nMessage: {message}',
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact_success')
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'temp_homepage/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'temp_homepage/contact_success.html')

# ... (keep other view functions as they are) ...