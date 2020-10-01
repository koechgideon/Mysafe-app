from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import File
from .forms import FileForm
from .enc import Cypher,ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'mysafe/home.html')

@login_required
def upload_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                myfile = request.FILES.get('file', None)
                password = request.POST.get('password', None)
                title = request.POST.get('title', None)
                about = request.POST.get('about', None)
                encrypted_file = Cypher().encrypt_file(myfile, password, extension='enc')
                files = File.objects.create(file=encrypted_file,title=title,about=about)
                files.save()
                return redirect('uploaded-files')
            except ValidationError as e:
                print(e)
            
    else:
        form = FileForm()
    
    return render(request, 'mysafe/upload.html', {'form': form})


def files(request):
    files = File.objects.all()
    return render(request, 'files.html', {
        'files': files
    })

def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('uploaded-files')

def about(request):
  return render(request,'mysafe/about.html',{'title':'About'})