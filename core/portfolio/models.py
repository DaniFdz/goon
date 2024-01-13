import os

from django.db import models
from PIL import Image


class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Clothe(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Set the maximum size in bytes (5MB)
        max_size_bytes = 1 * 1024 * 1024
        # Open the uploaded image file
        img = Image.open(self.image.path)

        # Check if the image is larger than the max size
        quality = 100
        while os.path.getsize(self.image.path) > max_size_bytes and quality > 0:
            # Reduce the quality
            img.save(self.image.path, quality=quality)

            quality -= 1

    def __str__(self):
        if self.category:
            return f"{self.category.name} - {self.name}"
        else:
            return self.name
