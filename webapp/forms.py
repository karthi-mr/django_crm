from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from webapp.models import Record


# ? Register / Create User
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

# ? Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    class Meta:
        pass

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'