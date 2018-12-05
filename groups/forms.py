from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Group


class GroupForm(forms.ModelForm):
    """Form definition for Group."""
    start_date = forms.DateField(
        widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")
        ),
        label='시작일'
    )

    time = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'예) 17:00 ~ 19:00'}))

    class Meta:
        """Meta definition for Groupform."""

        model = Group
        fields = (
            'name', 'photo', 'level', 'start_date', 'day',
            'time', 'duration', 'price', 'size', 'location',
            'description'
        )
