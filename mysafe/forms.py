from django import forms
from .models import myfile

class FileForm(forms.ModelForm):
    class Meta:
        model = myfile
        fields=('file','password','title','about')