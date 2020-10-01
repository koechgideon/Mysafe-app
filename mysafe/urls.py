from django.urls import path
from mysafe import views
 

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('files/', views.files, name='uploaded-files'),
    path('files/upload/', views.upload_files, name='upload-file'),
    path('files/<int:pk>/', views.delete_file, name='delete-file'),
    path('about/', views.about, name='mysafe-about')
] 