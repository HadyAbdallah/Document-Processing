from django.db import models
from PIL import Image
from PyPDF2 import PdfReader
import os

class UploadedImage(models.Model):
    file_path = models.ImageField(upload_to='images/')
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    channels = models.PositiveIntegerField(editable=False, null=True)

    def delete(self, *args, **kwargs):
        # Delete the file from the file system
        if self.file_path and os.path.isfile(self.file_path.path):
            os.remove(self.file_path.path)
        # Call the superclass delete method to remove the record from the database
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from PIL import Image
        with Image.open(self.file_path.path) as img:
            self.width, self.height = img.size
            self.channels = len(img.getbands())
        super().save(update_fields=['width', 'height', 'channels'])

class UploadedPDF(models.Model):
    file_path = models.FileField(upload_to='pdfs/')
    number_of_pages = models.PositiveIntegerField(editable=False, null=True)
    page_width = models.FloatField(editable=False, null=True)
    page_height = models.FloatField(editable=False, null=True)

    def delete(self, *args, **kwargs):
        # Delete the file from the file system
        if self.file_path and os.path.isfile(self.file_path.path):
            os.remove(self.file_path.path)
        # Call the superclass delete method to remove the record from the database
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open(self.file_path.path, 'rb') as f:
            reader = PdfReader(f)
            self.number_of_pages = len(reader.pages)
            first_page = reader.pages[0]
            self.page_width = first_page.mediabox.width
            self.page_height = first_page.mediabox.height
        super().save(update_fields=['number_of_pages', 'page_width', 'page_height'])