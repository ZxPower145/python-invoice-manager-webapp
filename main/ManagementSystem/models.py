from django.db import models

INVOICE_TYPE = (
    ("Receipt", "Receipt"),
    ("Proforma Invoice", "Proforma Invoice"),
    ("Invoice", "Invoice")
)


class Invoice(models.Model):
    comments = models.TextField('Comments', max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField('Invoice Number', unique=True)
    invoice_date = models.DateField('Invoice Date', auto_now_add=False, auto_now=False)
    name = models.CharField('Customer Name', max_length=120, default='')

    item_one = models.CharField('Item 1', max_length=200, default='')
    item_one_quantity = models.IntegerField('Quantity', default=0)
    item_one_unit_price = models.DecimalField('Unit Price (€)', default=0, decimal_places=2, max_digits=500000)
    item_one_total_price = models.DecimalField('Total (€)', default=0, decimal_places=2, max_digits=500000)

    item_two = models.CharField('Item 2', max_length=200, default='', null=True, blank=True)
    item_two_quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    item_two_unit_price = models.DecimalField('Unit Price (€)', default=0, decimal_places=2, max_digits=500000,
                                              null=True, blank=True)
    item_two_total_price = models.DecimalField('Total (€)', default=0, decimal_places=2, max_digits=500000,
                                               null=True, blank=True)

    item_three = models.CharField('Item 3', max_length=200, default='', null=True, blank=True)
    item_three_quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    item_three_unit_price = models.DecimalField('Unit Price (€)', default=0, decimal_places=2, max_digits=500000,
                                                null=True, blank=True)
    item_three_total_price = models.DecimalField('Total (€)', default=0, decimal_places=2, max_digits=500000,
                                                 null=True, blank=True)

    item_four = models.CharField('Item 4', max_length=200, default='', null=True, blank=True)
    item_four_quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    item_four_unit_price = models.DecimalField('Unit Price (€)', default=0, decimal_places=2, max_digits=500000,
                                               null=True, blank=True)
    item_four_total_price = models.DecimalField('Total (€)', default=0, decimal_places=2, max_digits=500000,
                                                null=True, blank=True)

    item_five = models.CharField('Item 5', max_length=200, default='', null=True, blank=True)
    item_five_quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    item_five_unit_price = models.DecimalField('Unit Price (€)', default=0, decimal_places=2, max_digits=500000,
                                               null=True, blank=True)
    item_five_total_price = models.DecimalField('Total (€)', default=0, decimal_places=2, max_digits=500000,
                                                null=True, blank=True)

    phone_number = models.CharField(max_length=120, default='', null=True, blank=True)
    total = models.DecimalField('Invoice Total (€)', decimal_places=2, max_digits=5000000, default=0)
    balance = models.DecimalField(decimal_places=2, max_digits=5000000, default=0, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    paid = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=50, default='', choices=INVOICE_TYPE)

    def __str__(self):
        return str(self.invoice_number) + ' - ' + self.name
