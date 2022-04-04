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
        verbose_name_plural = 'Вас'
        ordering = ['id']

class TypeOfModeling(models.Model):
    name = models.CharField(max_length=50,default=None,verbose_name='Вид моделирования')
    number = models.IntegerField(default=None,verbose_name='Кол-во проголосовавших')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип моделирования'
        verbose_name_plural = 'Типы моделирования'
        ordering = ['id']

class AnswersTable(models.Model):
    name = models.CharField(max_length=50, default=None, verbose_name='Имя ответа')
    answer1 = models.CharField(max_length=100, blank=True, verbose_name='ответ 1')
    answer2 = models.CharField(max_length=100, blank=True, verbose_name='ответ 2')
    answer3 = models.CharField(max_length=100, blank=True, verbose_name='ответ 3')
    answer4 = models.CharField(max_length=100, blank=True, verbose_name='ответ 4')
    answer5 = models.CharField(max_length=100, blank=True, verbose_name='ответ 5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель ответа'
        verbose_name_plural = 'Модели ответов'
        ordering = ['id']



class ProgramSettings(models.Model):
    forWho = models.CharField(max_length=100, default=None,verbose_name='Имя программы')
    devices = models.CharField(max_length=100, default='PC, Laptop, Phone',verbose_name='Устройства')
    cost = models.CharField(max_length=100, default='Free, Pay',verbose_name='Цена')
    subscription = models.BooleanField(blank=False,default=False,verbose_name='Подписка, если платно(если есть)')
    pay = models.IntegerField(blank=True,default=0,verbose_name='Цена программы или подписка(если есть)')
    using = models.CharField(max_length=100, default='Series, VideoGames, Models',verbose_name='Для чего используется')
    typeOfModeling = models.CharField(max_length=100, default='Solid, Polygonal, Sculpting',verbose_name='Какие типы моделирования используются')
    experience = models.CharField(max_length=100, default='Deep, Surface',verbose_name='Насколько глубоко изучение')
    prefabs = models.CharField(max_length=100, default='Help, Yourself',verbose_name='С готовыми моделями или самостоятельно')

    def __str__(self):
        return self.forWho

    class Meta:
        verbose_name = 'Настройки Программы'
        verbose_name_plural = 'Настройки Программ'
        ordering = ['id']


class ProgramsForBot(models.Model):
    name = models.CharField(max_length=100, default='Какое-то имя программы',verbose_name='Имя программы')
    settingsOfProgram = models.ForeignKey(ProgramSettings,on_delete=models.CASCADE,verbose_name='Ссылка на настройки программы')
    description = models.TextField(max_length=1000,default='описание',verbose_name='Описание программы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа для бота'
        verbose_name_plural = 'Программы для бота'
        ordering = ['id']
