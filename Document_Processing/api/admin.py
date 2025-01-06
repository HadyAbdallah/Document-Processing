from django.contrib import admin
from .models import UploadedImage, UploadedPDF

admin.site.register(UploadedImage)
admin.site.register(UploadedPDF)
