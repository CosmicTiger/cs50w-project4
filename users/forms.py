from django.forms.widgets import ClearableFileInput
from primitiva_project.settings import AUTH_USER_MODEL as User
from primitiva_staff.models import Staff
from django import forms

class RegisterFormStepOne(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=24, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=24, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RegisterFormStepTwo(forms.Form):
    identification_photo = forms.ImageField()
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    secondary_last_name = forms.CharField(max_length=100)
    profession = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=100)
    residence_city = forms.CharField(max_length=100)

    class Meta:
        model = Staff
        fields = ['identification_photo', 'first_name', 'middle_name'
                  'last_name', 'secondary_last_name', 'profession', 'address', 'phone', 'residence_city']
        widgets = {
            'identification_photo': ClearableFileInput(attrs={'multiple': False})
        }
