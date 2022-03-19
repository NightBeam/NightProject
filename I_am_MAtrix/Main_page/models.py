from django.db import models

# Create your models here.
class Redic(models.Model):
    WarRedirect = models.BooleanField()

class InfaAboutUs(models.Model):
    name = models.CharField(max_length=50, default='SOME NAME')
    text = models.TextField(max_length=500, default='SOME TEXT')
    dateOfCreation = models.DateField(auto_now_add=True)
    dateOfChenges = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Параграф для AboutUs'
        verbose_name_plural = 'Параграфы для AboutUs'
        ordering = ['id']


class ImagesOurWorks(models.Model):
    name = models.CharField(max_length=50, default='SOME NAME')
    image = models.ImageField(upload_to='imagesForOurWorks/')
    dateOfCreation = models.DateField(auto_now_add=True)
    dateOfChenges = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото для OurWorks'
        verbose_name_plural = 'Фотографии для OurWorks'
        ordering = ['id']