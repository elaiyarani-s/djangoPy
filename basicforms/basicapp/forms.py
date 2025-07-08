from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class BasicForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=500)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Invalid email address')
        return email
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message is None or len(message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        return message
    

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        
        if not name or not email:
            raise ValidationError("Both name and email are required.")
        
        return cleaned_data
