from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=32, required=True)
    email =  forms.EmailField(max_length=64,help_text="Enter a Valid email address here", required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username','email')


        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}),
        }