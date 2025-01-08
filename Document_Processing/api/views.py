from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadedImage, UploadedPDF
from .serializers import UploadedImageSerializer, UploadedPDFSerializer
import base64
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from rest_framework import generics, status

class UploadFileView(APIView):
    def post(self, request, *args, **kwargs):
        file_data = request.data.get('file')
        file_name = request.data.get('name')
        file_type = request.data.get('type')

        if not file_data or not file_name or not file_type:
            return Response({"error": "File data, name, and type are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = base64.b64decode(file_data)
            if file_type == 'image':
                image = UploadedImage(file_path=ContentFile(decoded_file, name=file_name))
                image.save()
                return Response(UploadedImageSerializer(image).data, status=status.HTTP_201_CREATED)
            elif file_type == 'pdf':
                pdf = UploadedPDF(file_path=ContentFile(decoded_file, name=file_name))
                pdf.save()
                return Response(UploadedPDFSerializer(pdf).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Unsupported file type."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
