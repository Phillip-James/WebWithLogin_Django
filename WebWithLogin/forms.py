from django import forms
from .models import profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['introduction']
        labels = {'text': ''}