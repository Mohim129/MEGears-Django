from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
        #     'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your review here...'}),
        #     'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'step': 0.1}),
        # }