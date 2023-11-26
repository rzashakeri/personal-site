from django import forms
from captcha.fields import CaptchaField
from pages.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    captcha = CaptchaField()

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
