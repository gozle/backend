from django.db import models

# Create your models here.
class RssModel(models.Model):
    title_tm = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    url = models.URLField()
    photo = models.ImageField(upload_to='downloads/', null=True)
    descriptoin_tm = models.TextField()
    descriptoin_en = models.TextField()
    descriptoin_ru = models.TextField()