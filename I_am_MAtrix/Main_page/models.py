from django.db import models
# Create your models here.
class Redic(models.Model):
    WarRedirect = models.BooleanField()

class InfaAboutUs(models.Model):
    name = models.CharField(max_length=50, default=None,verbose_name='Название поста')
    text = models.TextField(max_length=1000, default=None,verbose_name='Текст поста')
    dateOfCreation = models.DateField(auto_now_add=True)
    dateOfChenges = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Параграф для AboutUs'
        verbose_name_plural = 'Параграфы для AboutUs'
        ordering = ['id']


class VideoOurWorks(models.Model):
    name = models.CharField(max_length=50, default=None,verbose_name='Название видео')
    video = models.FileField(upload_to='videoForOurWorks/',default=None,verbose_name='Видео(ваша работа)')
    dateOfCreation = models.DateField(auto_now_add=True)
    dateOfChenges = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видео для OurWorks'
        verbose_name_plural = 'Видео для OurWorks'
        ordering = ['id']

class ProgramsInfa(models.Model):
    name = models.CharField(max_length=50, default=None,verbose_name='Имя программы')
    text = models.TextField(max_length=1000,default=None,verbose_name='Краткое описание программы')
    image = models.ImageField(upload_to='imagesForDocumentation/',default=None,verbose_name='Иконка программы')
    link1 = models.CharField(max_length=100, default=None,verbose_name='Первая ссылка программы')
    nameOfLink1 = models.CharField(max_length=50, default=None,verbose_name='Название первой ссылки программы')
    dateOfCreation = models.DateField(auto_now_add=True)
    dateOfChenges = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа для Documentation'
        verbose_name_plural = 'Программы для Documentation'
        ordering = ['id']


class We(models.Model):
    name = models.CharField(max_length=50,default=None,verbose_name='Ваше имя')
    vk = models.CharField(max_length=100,default=None,verbose_name='Ссылка на соц. сеть')
    foto = models.ImageField(upload_to='fotoWe/',default=None,verbose_name='Ваше фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вы'
        verbose_name_plural = 'вас'
        ordering = ['id']
