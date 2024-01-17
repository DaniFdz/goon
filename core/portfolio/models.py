import os
from uuid import uuid4

from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


def generate_filename(_, filename):
    if not filename:
        raise ValueError("Filename cannot be empty")
    ext = filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join("images/", filename)


class Clothe(models.Model):
    image = models.ImageField(upload_to=generate_filename)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.category:
            return f"{self.category.name} - {self.name}"
        else:
            return self.name
