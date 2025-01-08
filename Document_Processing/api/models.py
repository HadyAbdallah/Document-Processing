from django.db import models
from PIL import Image
from PyPDF2 import PdfReader

class UploadedImage(models.Model):
    file_path = models.ImageField(upload_to='images/')
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    channels = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with Image.open(self.file_path.path) as img:
            self.width, self.height = img.size
            self.channels = len(img.getbands())
        super().save(update_fields=['width', 'height', 'channels'])

class UploadedPDF(models.Model):
    file_path = models.FileField(upload_to='pdfs/')
    number_of_pages = models.PositiveIntegerField(editable=False)
    page_width = models.FloatField(editable=False)
    page_height = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open(self.file_path.path, 'rb') as f:
            reader = PdfReader(f)
            self.number_of_pages = len(reader.pages)
            first_page = reader.pages[0]
            self.page_width = first_page.mediabox.width
            self.page_height = first_page.mediabox.height
        super().save(update_fields=['number_of_pages', 'page_width', 'page_height'])