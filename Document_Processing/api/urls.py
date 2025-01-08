from django.urls import path
from .views import UploadFileView, ImageListView, PDFListView, ImageDetailView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('pdfs/', PDFListView.as_view(), name='pdf-list'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
]