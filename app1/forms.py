from django import forms
from models import Screenshot

class ScreenshotUploadForm(forms.ModelForm):
    image = forms.ImageField(error_messages={'required': 'Please upload an image!'})

    class Meta:
        model = Screenshot
        fields = ('image',)
        labels = {'image': 'Select an image to upload'}

