from django.db import models
from django.utils.translation import gettext as _

class Contact(models.Model):
    __tablename__ = 'contact'
    
    # information
    name = models.CharField(_('name'), max_length=30)
    email = models.EmailField(_('email'), max_length=125)
    message = models.TextField(_('message'))


    # moderations
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        
    def __str__(self):
        return self.name


class Subscriber(models.Model):
    __tablename__ = 'subscribers'
    # information
    mail = models.EmailField(_('email'), max_length=125, unique=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')
        
    def __str__(self):
        return self.mail