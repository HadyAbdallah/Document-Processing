from rest_framework import serializers
from models import UploadedPDF,UploadedImage

class ImageSerializer(serializers.ModelSerializers):
     class Meta:
        model = UploadedImage
        fields = '__all__'
        read_only_fields = ['width', 'height', 'channels', 'uploaded_at']


class PdfSerializer(serializers.ModelSerializers):
    class Meta:
        model = UploadedPDF
        fields = '__all__'
        read_only_fields = ['number_of_pages', 'page_width', 'page_height', 'uploaded_at']