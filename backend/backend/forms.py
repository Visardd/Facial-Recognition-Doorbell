from django import forms
from .models import image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'Main_img']