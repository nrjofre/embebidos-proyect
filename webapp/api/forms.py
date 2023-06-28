from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError

from api.models import Document
from api.models import User
from api.models import Retrieve

# Create your views here.

class RegisterForm(UserCreationForm):
    username = UsernameField(label='Rut', widget=forms.TextInput(attrs={'autofocus': True}), required=True)
    #is_staff = forms.BooleanField(label="Admin", required=False)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class DocumentForm(ModelForm):
    password = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Document
        fields = ["rut", "password","name", "dispenser_slot"]

    def clean(self):
        cleaned_data = super().clean()
        dispenser_slot = cleaned_data.get("dispenser_slot")

        # Check if the slot is already occupied
        if Document.objects.filter(dispenser_slot=dispenser_slot).exists():
            raise ValidationError("The slot is already occupied.")

        return cleaned_data

class RetrieveForm(ModelForm):
    rut = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Retrieve
        fields = ["rut", "password"]