from django.urls import path
from .views import UploadFileView, ImageListView, PDFListView, ImageDetailView
from .views import PDFDetailView, RotateImageView, ConvertPDFToImageView

# Define URL patterns for the API views
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('pdfs/', PDFListView.as_view(), name='pdf-list'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('pdfs/<int:pk>/', PDFDetailView.as_view(), name='pdf-detail'),
    path('rotate/', RotateImageView.as_view(), name='rotate-image'),
    path('convert-pdf-to-image/', ConvertPDFToImageView.as_view(), name='convert-pdf-to-image'),
]