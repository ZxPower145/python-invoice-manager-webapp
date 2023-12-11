from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'name', 'invoice_date', 'paid', 'total']
    form = InvoiceForm
    list_filter = ['name', 'invoice_number', 'invoice_date', 'paid']
    search_fields = ['name', 'invoice_number', 'invoice_date', 'total']
    ordering = ('-invoice_number',)


admin.site.register(Invoice, InvoiceAdmin)
