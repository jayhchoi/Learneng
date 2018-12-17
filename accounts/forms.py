from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class SignupForm(UserCreationForm):
    username = forms.CharField(label='ID')
    email = forms.EmailField(label='이메일', max_length=254)
    name = forms.CharField(label='성명', max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     username = self.cleaned_data.get('username')
    #     if email and User.objects.filter(email=email).exclude(username=username).exists():
    #         raise forms.ValidationError('해당 이메일로 가입된 회원이 이미 있습니다')
    #     return email

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_member = True
    #     if commit:
    #         user.save()
    #     return user


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='ID')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']

