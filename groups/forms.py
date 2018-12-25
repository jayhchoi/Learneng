from django import forms
from django.forms.widgets import SelectDateWidget
from django.utils import timezone

from .models import Group


class GroupForm(forms.ModelForm):
    """Form definition for Group."""
    start_date = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'datepicker'}),
        label='시작일'
    )
    photo = forms.ImageField(label='메인 이미지(Optional)', required=False)
    size = forms.IntegerField(label='정원(최대 8명)')

    time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'예) 17:00 ~ 19:00'}),
        label='시간'
    )

    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'예) 홍대'}),
        label='지역'
    )

    class Meta:
        model = Group
        fields = (
            'name', 'photo', 'level', 'start_date', 'day',
            'time', 'duration', 'price', 'size', 'location',
            'description'
        )


# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea)