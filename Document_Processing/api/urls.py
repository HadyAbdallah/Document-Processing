from django.urls import path
from .views import UploadFileView, ImageListView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('images/', ImageListView.as_view(), name='image-list')
]