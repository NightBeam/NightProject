# Generated by Django 4.0 on 2022-04-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0018_programsforbot_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programsforbot',
            name='description',
            field=models.TextField(default='описание', max_length=1000, verbose_name='Описание программы'),
        ),
    ]
