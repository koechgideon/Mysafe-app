from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class myfile(models.Model):
    file=models.FileField(upload_to='files/encrypted')
    password=models.CharField(max_length=10,blank=True,null=True,default=None)
    date_posted=models.DateTimeField(default=timezone.now)
    objects=models.Manager() 
    
    def __str__(self):
        return str(self.file)
    def get_absolute_url(self):
        return reverse("landing-page", kwargs={"pk": self.pk})

class Dfile(models.Model):
    decryptedFile=models.FileField(upload_to='files/decrypted')
    password=models.CharField(max_length=10,blank=True,null=True,default=None)
    date_posted=models.DateTimeField(default=timezone.now)
    objects=models.Manager() 
    
    def __str__(self):
        return str(self.decryptedFile)
    def get_absolute_url(self):
        return reverse("landing-page", kwargs={"pk": self.pk})

    '''def save(self, *args, **kwargs):
        self.file.name = os.path.basename(self.file.name)
        return super(myfile, self).save(*args, **kwargs)'''
    


