from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Contact, Subscriber


class ContactForm(forms.ModelForm):

    class Meta:
            model = Contact
            fields = (
                'name',
                'email',
                'message',  
            )

            widgets = {
                
                'name': forms.TextInput(attrs={
                    
                    'class': 'form-control col-6 ',
                    'placeholder': 'Name'
                    
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control col-6 ',
                    'placeholder': 'E-mail adress'
                }),
                'message': forms.Textarea(attrs={
                    "rows": "5",
                    'class': 'form-control col-12 form-group-textarea',
                    'placeholder': 'Send Message...',
                    
                }),
                
            }

class SubscriberForm(forms.ModelForm):
    mail = forms.EmailField(max_length=125, widget=forms.EmailInput(attrs={
        'class': 'form-control pl-3 shadow-none bg-transparent border-0', 
        'placeholder': 'Enter your email address'
    }), )

    class Meta:
        model = Subscriber
        fields = (
            'mail',
        )


