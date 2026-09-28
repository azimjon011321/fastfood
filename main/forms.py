from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "address"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ismingiz",
                "class": "form-control",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "+998 90 123 45 67",
                "class": "form-control",
            }),
            "address": forms.Textarea(attrs={
                "placeholder": "Manzilingiz",
                "class": "form-control",
                "rows": 3,
            }),
        }