from django import forms
from .models import Invoice, InvoiceItem
from django.utils import timezone

class InvoiceAddModelForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ['is_approved', 'is_completed', 'is_valid']
        widgets = {
            'serial_num': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True,
                    'value': timezone.now().astimezone().strftime('%Y%m%d%H%M%S'),
                }
            ),
            'employee': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'filldate': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'value': timezone.now().astimezone().strftime('%Y-%m-%d'),
                }
            ),
            'request_unit': forms.Select(attrs={'class': 'custom-select'}),
            'pay_comp': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'pay_methold': forms.Select(attrs={'class': 'custom-select'}),
            'pay_currency': forms.Select(attrs={'class': 'custom-select'}),
            'pay_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'})
        }

class InvoiceUpdateModelForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ['serial_num', 'is_completed', 'is_approved', 'is_valid']
        widgets = {
            'employee': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'filldate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'request_unit': forms.Select(attrs={'class': 'custom-select'}),
            'pay_comp': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'pay_methold': forms.Select(attrs={'class': 'custom-select'}),
            'pay_currency': forms.Select(attrs={'class': 'custom-select'}),
            'pay_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }

class InvoiceItemAddModelForm(forms.ModelForm):

    class Meta:
        model = InvoiceItem
        fields = '__all__'
        widgets = {
            'invoice_sn': forms.NumberInput(),
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\S+.*'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }