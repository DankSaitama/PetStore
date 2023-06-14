from django import forms
from django.contrib.auth.models import User


#Models
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','password','password2','email']

class PetImage(forms.Form):
    file = forms.FileField()


