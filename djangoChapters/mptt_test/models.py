# models.py
from django.db import models
from mptt.fields import TreeForeignKey as MpttTreeForeignKey
from mptt.models import MPTTModel
from multiupload.fields import MultiFileField

class File(models.Model):
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='chapter_files/')

class Chapter(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    context = models.TextField(blank=True, null=True)
    parent = MpttTreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
