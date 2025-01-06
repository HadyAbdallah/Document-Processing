from django.db import models
from PIL import Image
from PyPDF2 import PdfReader

class UploadedImage(models.Model):
    file_path = models.ImageField(upload_to='images/')
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    channels = models.PositiveIntegerField(editable=False)

    # def save(self, *args, **kwargs):
    #     # Call the original save method to ensure the file is saved
    #     super().save(*args, **kwargs)

    #     # Open the image file to extract metadata
    #     with Image.open(self.file_path.path) as img:
    #         self.width, self.height = img.size
    #         self.channels = len(img.getbands())

    #     # Save the instance again to update the metadata fields
    #     super().save(update_fields=['width', 'height', 'channels'])

    # def __str__(self):
    #     return f"Image {self.id}: {self.file_path.name}"


class UploadedPDF(models.Model):
    file_path = models.FileField(upload_to='pdfs/')
    number_of_pages = models.PositiveIntegerField(editable=False)
    page_width = models.FloatField(editable=False)
    page_height = models.FloatField(editable=False)

    # def save(self, *args, **kwargs):
    #     # Call the original save method to ensure the file is saved
    #     super().save(*args, **kwargs)

    #     # Open the PDF file to extract metadata
    #     with open(self.file_path.path, 'rb') as f:
    #         reader = PdfReader(f)
    #         self.number_of_pages = len(reader.pages)
    #         # Assuming all pages have the same size, get the size of the first page
    #         first_page = reader.pages[0]
    #         self.page_width = first_page.mediabox.width
    #         self.page_height = first_page.mediabox.height

    #     # Save the instance again to update the metadata fields
    #     super().save(update_fields=['number_of_pages', 'page_width', 'page_height'])

    # def __str__(self):
    #     return f"PDF {self.id}: {self.file_path.name}"