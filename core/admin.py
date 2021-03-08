from core.models import Contact
from django.contrib import admin
from .models import Contact, Subscriber
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register([Contact, Subscriber])
admin.site.unregister(Group)

admin.site.site_header = "FAA"
admin.site.index_title = "The Federation of Azerbaijani Americans"
admin.site.site_title = "FAA Administration"