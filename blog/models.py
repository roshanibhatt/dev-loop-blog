from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Blog (models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    Content=HTMLField()
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title