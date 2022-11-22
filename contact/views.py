from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Envio de correo y redireccion
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje",
                f"De {name} <{email}>\n\nMensaje:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["chinop2799@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo salio bien, redireccion a ok
                return redirect(reverse('contact:contact')+ "?ok")
            except:
                #Salio mal, redireccion a fail
                return redirect(reverse('contact:contact')+ "?fail")
            
    return render(request, "contact/contact.html", {'form': contact_form})