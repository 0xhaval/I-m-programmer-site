from django import forms


class ContactForm(forms.Form):
    yourName = forms.CharField(max_length=200, label='Your Name')
    email = forms.CharField(required=True, label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
