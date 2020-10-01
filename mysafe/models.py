from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class File(models.Model):
    file=models.FileField(upload_to='files/encrypted')
    password=models.CharField(max_length=10,blank=True,null=True,default=None)
    title=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    objects=models.Manager() 
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("files-posted", kwargs={"pk": self.pk})
    
    


