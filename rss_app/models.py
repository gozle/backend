from django.db import models

# Create your models here.

class Source(models.Model):
    LANG_CHOICES = [
        ('ru', 'RU'),
        ('en', "EN"),
        ('tm', 'TM')
    ]
    name = models.CharField(max_length=255)
    link = models.URLField()
    language = models.CharField(max_length=3 , choices=LANG_CHOICES)
    icon = models.ImageField(upload_to='source_icon/', null=True)
    rss_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Source'

    def __str__(self):
        return self.name

class News(models.Model):
    source  = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='source_news')
    guid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    summary = models.TextField(null=True)
    content = models.TextField(null=True)
    photo = models.ImageField(upload_to='item_photos/', null=True)
    url = models.URLField()
    view = models.IntegerField(default=0)
    pubDate = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
