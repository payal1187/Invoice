from django.contrib import admin
from invoice_app.models import *

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
