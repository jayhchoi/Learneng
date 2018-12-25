from django import forms

from .models import Comment

RATING_CHOICES = (
    ('', '별점 주기'),
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
)

class CommentForm(forms.ModelForm):
    """Form definition for Comment."""
    body = forms.CharField(label=False, widget=forms.Textarea(attrs={
        "placeholder": "리더님에 대한 리뷰를 달아주세요!",
    }))

    rating = forms.ChoiceField(label=False, choices=RATING_CHOICES)

    class Meta:
        model = Comment
        fields = (
            'body',
            'rating'
        )