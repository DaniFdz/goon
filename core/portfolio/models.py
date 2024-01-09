from django.core.exceptions import ValidationError
from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 50.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class Clothe(models.Model):
    image = models.ImageField(upload_to="images/", validators=[validate_image])
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.category:
            return f"{self.category.name} - {self.name}"
        else:
            return self.name
