# Generated by Django 4.0 on 2022-04-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0016_alter_programsettings_typeofmodeling'),
    ]

    operations = [
        migrations.AddField(
            model_name='programsettings',
            name='pay',
            field=models.IntegerField(blank=True, default=0, verbose_name='Цена программы или подписка(если есть)'),
        ),
    ]
