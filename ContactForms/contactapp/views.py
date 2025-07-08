from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('thankyou')
    else:
        form = ContactForm()

    return render(request, 'contact/contactus_form.html', {'form': form})

def thank_you(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/thankyou.html', {'contacts': contacts})
