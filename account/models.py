import uuid
from django.conf import settings
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models import Subscriber
from .managers import UserManager


class DonationUser(models.Model):
    full_name = models.CharField(_('full name'), max_length=80, blank=True)
    membership_id = models.CharField(_("Membership id"), max_length=1000000, default='', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    birthday = models.DateField(_("Birthday"), auto_now_add=False, auto_now=False, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=30, blank=True)
    citizenship = models.CharField(_('citizenship'), max_length=225, blank=True)
    education = models.CharField(_('education'), max_length=225, blank=True)
    current = models.CharField(_('current'), max_length=225, blank=True)
    permoment = models.CharField(_('permoment'), max_length=225)
    member_of_ngo = models.CharField(_('member of ngo'), max_length=225, blank=True)
    usa_year = models.IntegerField(_('usa year'), null=True)
    reasons = models.TextField(_('reasons'), blank=True)
    mention = models.TextField(_('mention'), blank=True)


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_("Active"), default=False)


    class Meta:
        """Meta definition for Contact."""
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        super(DonationUser, self).save(*args, **kwargs)
        raw_id = uuid.uuid1()
        raw_membership_id = str(raw_id.int)[:6]
        self.membership_id = f'{raw_membership_id}{self.id}'
        if self.is_active == True:
            send_mail('subject', f'This is you membership id {self.membership_id}', 'husubayli@gmail.com', [self.email,])
        else:
            send_mail('subject', f'Your form on review', 'husubayli@gmail.com', [self.email,])
        super(DonationUser, self).save(*args, **kwargs)

    USERNAME_FIELD = ['membership_id']

    objects = UserManager()

    def __str__(self):
        created_date = self.created_at.date()
        return  f'{self.email}'
            
    
    def get_absolute_url(self):
        return reverse_lazy("account:profile", kwargs={"membership_id": self.membership_id})
    

class Message(models.Model):
    subject = models.CharField(_('Subject'), max_length=80, blank=True)
    content = models.TextField(_('Content'), blank=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        subscribers = [i for i in Subscriber.objects.all()]
        print(subscribers)
        for subscriber in subscribers:
            send_mail(self.subject, self.content, 'husubayli@gmail.com', [subscriber.mail])
        super(Message, self).save(*args, **kwargs)