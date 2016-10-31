from django import forms

from .models import Subscription
from landingpage.tasks import send_welcome_email_task


class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Subscription
        fields = ('name', 'email', )

    # def send_email(self):
    #     send_welcome_email_task.delay(
    #         self.cleaned_data['name'], self.cleaned_data['email'])
