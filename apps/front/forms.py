from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-gray-200 px-4 py-3 text-gray-900 focus:border-sky-500 focus:outline-none focus:ring-1 focus:ring-sky-500',
                'placeholder': 'Ismingiz'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-md border border-gray-200 px-4 py-3 text-gray-900 focus:border-sky-500 focus:outline-none focus:ring-1 focus:ring-sky-500',
                'placeholder': 'sizning.email@misol.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full rounded-md border border-gray-200 px-4 py-3 text-gray-900 focus:border-sky-500 focus:outline-none focus:ring-1 focus:ring-sky-500',
                'placeholder': 'Qanday yordam bera olaman?',
                'rows': 5
            }),
        }
