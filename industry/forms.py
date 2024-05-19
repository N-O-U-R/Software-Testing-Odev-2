from django import forms
from .models import Industry

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['title', 'description', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }
