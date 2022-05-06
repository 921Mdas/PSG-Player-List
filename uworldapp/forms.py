
from django import forms

class seeForm(forms.Form):
    name = forms.CharField(label="enter name")
    email = forms.EmailField(label="enter email")
    message = forms.CharField(widget=forms.Textarea)
    date = forms.CharField(widget=forms.DateInput)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass