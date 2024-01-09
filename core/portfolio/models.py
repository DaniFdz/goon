from django.db import models


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

    def __str__(self):
        if self.category:
            return f"{self.category.name} - {self.name}"
        else:
            return self.name
