from django.db import models
from django.utils.text import slugify


class Conference(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='imgs/')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class WordPart(models.Model):
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name='word_parts'
    )
    maqola_soni = models.IntegerField()
    bet_soni = models.IntegerField()
    yaratilgan_sana = models.DateField(auto_now_add=True)
    word_fayl = models.FileField(upload_to='word_files/')
    content = models.TextField()
class Shoba(models.Model):
    conference = models.ForeignKey(
            Conference,
            on_delete=models.CASCADE,
            related_name='shoba'
        )
    title = models.TextField()
    content = models.TextField()
    img = models.ImageField(upload_to='imgs/')
    is_active = models.BooleanField(default=False)
    yaratilgan_sana = models.DateField(auto_now_add=True)
class Maqola(models.Model):
    shoba = models.ForeignKey(
            Conference,
            on_delete=models.CASCADE,
            related_name='maqola'
        )
    title = models.TextField()
    content = models.TextField()
    yaratilgan_sana = models.DateField(auto_now_add=True)
    word_fayl = models.FileField(upload_to='word_files/')
    