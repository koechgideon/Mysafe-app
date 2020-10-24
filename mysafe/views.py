from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import myfile, Dfile
from .forms import FileForm, DFileForm
from .enc import Cypher,ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files import File



@login_required
def home(request):
    return render(request, 'mysafe/home.html')

@login_required
def upload_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                ufile = request.FILES.get('file', None)
                password = request.POST.get('password', None)
                encrypted_file = Cypher().encrypt_file(ufile, password, extension='enc')
                files = myfile.objects.create(file=encrypted_file)
                files.save()
                return redirect('uploaded-files')
            except ValidationError as e:
                print(e)
            
    else:
        form = FileForm()
    
    return render(request, 'mysafe/upload.html', {'form': form})

@login_required
def files_view(request):
    files = myfile.objects.all()
    return render(request, 'files.html', {
        'files': files
    })
    
@login_required
def decrypt_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Decfile = request.FILES.get('file', None)
                password = request.POST.get('password', None)
                decrypted_file = Cypher().decrypt_file(Decfile, password, extension='enc')
                dfiles = Dfile.objects.create(decryptedFile=decrypted_file)
                dfiles.save()
                return redirect('Decrypted-files')
            except ValidationError as e:
                print(e)
            
    else:
        form = DFileForm()
    
    return render(request, 'mysafe/upload.html', {'form': form})

@login_required
def decryptedFiles_view(request):
    files = Dfile.objects.all()
    return render(request, 'dfiles.html', {
        'files': files
    })

def delete_file(request, pk):
    if request.method == 'POST':
        file = myfile.objects.get(pk=pk)
        file.delete()
    return redirect('uploaded-files')

def about(request):
  return render(request,'mysafe/about.html',{'title':'About'})