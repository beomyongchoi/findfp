from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Subscription
        fields = ('name', 'email', )

    # def clean_email(self):
    #     data = self.cleaned_data.get('email')
    #     if Subscription.objects.filter(email=data).exists():
    #         raise forms.ValidationError("This email already used")
    #     return data
