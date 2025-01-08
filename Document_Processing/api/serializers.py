from rest_framework import serializers
from .models import UploadedImage,UploadedPDF

class UploadedImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = UploadedImage
        fields = ['id', 'file_path', 'width', 'height', 'channels']
        read_only_fields = ['width', 'height', 'channels']


class UploadedPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedPDF
        fields = ['id', 'file_path', 'number_of_pages', 'page_width', 'page_height']
        read_only_fields = ['number_of_pages', 'page_width', 'page_height']