from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
