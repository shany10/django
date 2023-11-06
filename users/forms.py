""" from django import forms
from .models import MyUsers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import random
import string


class RegistrationForm(UserCreationForm):
    # Add your custom fields here
    nom = forms.CharField(max_length=30, required=True)
    prenom = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    adresse = forms.CharField(max_length=100, required=True)
    role = forms.ChoiceField(choices=(('instructeur', 'Insctructeur'), ('etudiant', 'Etudiant')), required=True)

    class Meta:
        model = MyUsers
        fields = ['last_name', 'first_name', 'email', 'addresse', 'password', 'user_type']

        
    def generate_random_password(self):
        # Generate a random password using letters and digits
        password_length = 12  # You can adjust the password length as needed
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(password_length))

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.generate_random_password()
        user.set_password(password)
        if commit:
            user.save()
        return user """
        
from django import forms

from .models import MyUsers

class MyUsersForm(forms.ModelForm):
    class Meta:
        model = MyUsers
        fields = ['first_name', 'last_name', 'email', 'forfait', 'address', 'user_type']
        labels = {
            'first_name' : 'Nom',
            'last_name': 'Prenom',
            'email': 'Email',
            'forfait': 'Forfait',
            'address': 'Addresse',
            'user_type': 'Type',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'forfait': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }