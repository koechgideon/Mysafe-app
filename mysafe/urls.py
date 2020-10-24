from django.urls import path
from mysafe import views
 

urlpatterns = [
    path('', views.files_view, name='landing-page'),
    path('files/upload/', views.upload_files, name='upload-file'),
    path('files/decrypt/', views.decrypt_files, name='decrypt-file'),
    path('files/encrypted', views.files_view, name='uploaded-files'),
    path('files/decrypted', views.decryptedFiles_view, name='decryped-files'),
    path('files/<int:pk>/', views.delete_file, name='delete-file'),
    path('about/', views.about, name='mysafe-about')
] 