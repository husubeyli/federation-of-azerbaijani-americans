from core.models import Contact
from django.urls.base import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactForm, SubscriberForm




class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        contact_form = ContactForm(prefix='contact_form')
        subscribers_form = SubscriberForm(prefix='subscribers_form')
        context = {
            'contact_form': contact_form,
            'subscribers_form': subscribers_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        contact_form = ContactForm(prefix='contact_form')
        subscribers_form = SubscriberForm(prefix='subscribers_form')
        
        action = self.request.POST['action']

        if action == 'contact_us':
            contact_form = ContactForm(request.POST, prefix='contact_form')
            if contact_form.is_valid():
                contact_form.save()
                return redirect('core:index', permanent=True)
        if action == 'subscribe':
            subscribers_form = SubscriberForm(request.POST, prefix='subscribers_form')
            if subscribers_form.is_valid():
                subscribers_form.save()
                return redirect('core:index')
        context = {
            'contact_form': contact_form,
            'subscribers_form': subscribers_form
        }
        return render(request, self.template_name, context)


