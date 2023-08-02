
from django import forms
from .models import FurnitureInfo

class FurnitureCreate(forms.ModelForm):
    class Meta:
        model = FurnitureInfo
        fields = '__all__'