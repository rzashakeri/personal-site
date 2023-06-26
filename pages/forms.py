from django import forms

from portfolio.pages.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First Name"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email"
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Your Message"
                }
            )
        }
