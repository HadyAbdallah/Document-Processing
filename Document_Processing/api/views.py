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
from pdf2image import convert_from_path

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

class ImageListView(generics.ListAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

class PDFListView(generics.ListAPIView):
    queryset = UploadedPDF.objects.all()
    serializer_class = UploadedPDFSerializer

class ImageDetailView(generics.RetrieveDestroyAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

class PDFDetailView(generics.RetrieveDestroyAPIView):
    queryset = UploadedPDF.objects.all()
    serializer_class = UploadedPDFSerializer

class RotateImageView(APIView):
    def post(self, request, *args, **kwargs):
        image_id = request.data.get('image_id')
        angle = request.data.get('angle')

        try:
            image = UploadedImage.objects.get(id=image_id)
            with Image.open(image.file_path.path) as img:
                rotated_image = img.rotate(angle, expand=True)
                buffer = BytesIO()
                rotated_image.save(buffer, format='JPEG')
                return Response({"rotated_image": base64.b64encode(buffer.getvalue()).decode()}, status=status.HTTP_200_OK)
        except UploadedImage.DoesNotExist:
            return Response({"error": "Image not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 

class ConvertPDFToImageView(APIView):
    def post(self, request, *args, **kwargs):
        pdf_id = request.data.get('pdf_id')

        try:
            pdf = UploadedPDF.objects.get(id=pdf_id)
            poppler_path = r'E:\RDI Task\poppler-24.08.0\Library\bin'  # Adjust this path to where Poppler is installed
            images = convert_from_path(pdf.file_path.path, poppler_path=poppler_path)
            
            # List to hold base64-encoded images
            encoded_images = []

            for image in images:
                buffer = BytesIO()
                image.save(buffer, format='JPEG')
                encoded_image = base64.b64encode(buffer.getvalue()).decode()
                encoded_images.append(encoded_image)

            return Response({"images": encoded_images}, status=status.HTTP_200_OK)
        except UploadedPDF.DoesNotExist:
            return Response({"error": "PDF not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)