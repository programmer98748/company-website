from django.shortcuts import render, redirect
from django.contrib import auth, messages

#from dashboard.models import *
# Create your views here.
#from .forms import *

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.contrib import messages
#from .forms import ContactForm  # Assuming ContactForm is defined in your app


from django.core.mail import EmailMessage, send_mail,EmailMultiAlternatives

def send_contact_email(form_data):
    sender_email = form_data['email']  # Get sender's email from form data

    subject = 'رسائل للعميل'

    message = (
        'تلقيت رسالة جديدة من:\n '
        f'\u202eالاسم: {form_data["full_name"]}\u202f\n '  # Right-align name
        f'البريد الإلكتروني: {sender_email}\n '
        f'رقم الهاتف: {form_data["mobile"]}\n '  # Include mobile number if relevant
        f'الخدمة المطلوبة: {form_data["subject"]}\n '  # Include subject from dropdown
        f'الرسالة: {form_data["message"]}\n '
    )

    plain_message = message.replace('\n', '<br>')  # Replace newlines with HTML line breaks
    plain_message = html2text(plain_message)  # Convert HTML to plain text

    try:
        message = EmailMultiAlternatives(
            subject,
            body=plain_message,  # Pass message content as 'body' parameter
            from_email= form_data['email'],
            to=['jbgonna5@gmail.com'],
            reply_to=[sender_email],
        )
        message.send()
        print('jj')

    except BadHeaderError:
        print('Invalid header found in email. Check content.')  # Log the error for debugging
        return False  # Indicate unsuccessful email sending
    except Exception as e:  # Add generic exception handling
        print(f'Error sending email: {e}')
        return False

    return True  # Indicate successful email sending

def index(request):
    
    return render(request, 'website/index.html')


def project(request):


    return render(request, 'website/project.html')

def services(request):


    return render(request, 'website/pages/services.html')
