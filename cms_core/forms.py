from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)