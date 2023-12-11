from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice
from datetime import date
import sqlite3


def get_last_invoice_number():
    try:
        last_invoice_number = Invoice.objects.count()
    except Exception as e:
        print(e)
        last_invoice_number = 1
    return last_invoice_number + 1 if last_invoice_number else 1


class InvoiceForm(forms.ModelForm):
    INVOICE_TYPE = (("Receipt", "Receipt"),
                    ("Proforma Invoice", "Proforma Invoice"),
                    ("Invoice", "Invoice"))
    invoice_number = forms.IntegerField(
        required=True,
        label='',
        widget=forms.NumberInput(
            attrs={'class': 'text-center form-control',
                   'readonly': 'True'
                   }
        )
    )
    invoice_date = forms.DateField(
        initial=date.today(),
        label='',
        required=True,
        widget=forms.DateInput(
            attrs={'class': 'text-center form-control'
                   }
        )
    )
    total = forms.DecimalField(
        label='',
        widget=forms.NumberInput(
            attrs={'class': 'text-center form-control',
                   'readonly': 'readonly',
                   }
        )
    )

    class Meta:
        model = Invoice
        fields = [
            'invoice_number', 'name', 'phone_number', 'invoice_date',
            'item_one', 'item_one_quantity', 'item_one_unit_price', 'item_one_total_price',
            'item_two', 'item_two_quantity', 'item_two_unit_price', 'item_two_total_price',
            'item_three', 'item_three_quantity', 'item_three_unit_price', 'item_three_total_price',
            'item_four', 'item_four_quantity', 'item_four_unit_price', 'item_four_total_price',
            'item_five', 'item_five_quantity', 'item_five_unit_price', 'item_five_total_price',
            'total', 'paid', 'invoice_type'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['invoice_number'].initial = get_last_invoice_number()



class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model = Invoice
        novalidate = True
        fields = ["invoice_number", "name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['novalidate'] = 'novalidate'
            field.widget.attrs.pop('required', None)


class InvoiceUpdateForm(forms.ModelForm):
    INVOICE_TYPE = (("Receipt", "Receipt"),
                    ("Proforma Invoice", "Proforma Invoice"),
                    ("Invoice", "Invoice"))

    invoice_number = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'text-center form-control',
                   'readonly': 'True'}
        )
    )
    invoice_date = forms.DateField(
        initial=date.today(),
        required=True,
        widget=forms.DateInput(
            attrs={'class': 'text-center form-control'
                   }
        )
    )
    total = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'class': 'text-center form-control',
                   'readonly': 'True',
                   }
        )
    )
    item_one_total_price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'text-center form-control',
                'readonly': 'True'
            }
        )
    )
    item_two_total_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'text-center form-control',
                'readonly': 'True',
            }
        )
    )
    item_three_total_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'text-center form-control',
                'readonly': 'True',
            }
        )
    )
    item_four_total_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'text-center form-control',
                'readonly': 'True',
            }
        )
    )
    item_five_total_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'text-center form-control',
                'readonly': 'True',
            }
        )
    )
    class Meta:
        model = Invoice
        fields = [
            'invoice_number', 'name', 'phone_number', 'invoice_date',
            'item_one', 'item_one_quantity', 'item_one_unit_price', 'item_one_total_price',
            'item_two', 'item_two_quantity', 'item_two_unit_price', 'item_two_total_price',
            'item_three', 'item_three_quantity', 'item_three_unit_price', 'item_three_total_price',
            'item_four', 'item_four_quantity', 'item_four_unit_price', 'item_four_total_price',
            'item_five', 'item_five_quantity', 'item_five_unit_price', 'item_five_total_price',
            'total', 'paid', 'invoice_type'
        ]


class SignUp(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'required': '',
                'name': 'username',
                'id': 'username',
                'type': 'text',
                'class': 'username',
                'placeholder': 'User Name',
                'maxlength': '16',
                'minlength': '4',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'required': '',
                'null': 'False',
                'name': 'email',
                'id': 'email',
                'type': 'email',
                'class': 'email',
                'placeholder': 'Email Address',
                'maxlength': '30',
                'minlength': '6',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'required': '',
                'name': 'password1',
                'id': 'password1',
                'type': 'password',
                'class': 'password',
                'placeholder': 'Password',
                'maxlength': '16',
                'minlength': '8',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'required': '',
                'name': 'password2',
                'id': 'password2',
                'type': 'password',
                'class': 'password',
                'placeholder': 'Repeat Password',
                'maxlength': '16',
                'minlength': '8',
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
