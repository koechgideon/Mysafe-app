from django import forms
from .models import myfile,Dfile

class FileForm(forms.ModelForm):
    class Meta:
        model = myfile
        fields=('file','password')
        
class DFileForm(forms.ModelForm):
    class Meta:
        model = Dfile
        fields=('decryptedFile','password')