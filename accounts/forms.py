from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=30, help_text='Required. Enter your full name.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     if commit:
    #         user.save()
    #     return user