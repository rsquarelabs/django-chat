from django import forms
from core.models import User
from django.utils.translation import ugettext_lazy as _
import logging
from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)

class RegistrationForm(forms.Form):
    first_name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("User Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Confirm Password"))
#     agree_terms = forms.BooleanField(required=True, label="I agree to the Terms & Conditions")
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data