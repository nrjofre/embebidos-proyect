from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField

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
        fields = ["user", "password","name", "dispenser_slot"]

class RetrieveForm(ModelForm):
    rut = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Retrieve
        fields = ["rut", "password"]