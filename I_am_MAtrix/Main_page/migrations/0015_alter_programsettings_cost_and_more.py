# Generated by Django 4.0 on 2022-04-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0014_programsettings_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programsettings',
            name='cost',
            field=models.CharField(default='Free, Pay', max_length=100, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='devices',
            field=models.CharField(default='PC, Laptop, Phone', max_length=100, verbose_name='Устройства'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='experience',
            field=models.CharField(default='Deep, Surface', max_length=100, verbose_name='Насколько глубоко изучение'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='forWho',
            field=models.CharField(default=None, max_length=100, verbose_name='Имя программы'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='prefabs',
            field=models.CharField(default='Help, Yourself', max_length=100, verbose_name='С готовыми моделями или самостоятельно'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='subscription',
            field=models.BooleanField(default=False, verbose_name='Подписка, если платно(если есть)'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='typeOfModeling',
            field=models.CharField(default='Solid, Polygonal, Sculpting', max_length=100, verbose_name='Какие типы моделирования используется'),
        ),
        migrations.AlterField(
            model_name='programsettings',
            name='using',
            field=models.CharField(default='Series, VideoGames, Models', max_length=100, verbose_name='Для чего используется'),
        ),
        migrations.AlterField(
            model_name='programsforbot',
            name='name',
            field=models.CharField(default='Какое-то имя программы', max_length=100, verbose_name='Имя программы'),
        ),
        migrations.AlterField(
            model_name='programsforbot',
            name='settingsOfProgram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_page.programsettings', verbose_name='Ссылка на настройки программы'),
        ),
    ]
