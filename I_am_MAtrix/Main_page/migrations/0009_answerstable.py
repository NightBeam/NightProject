# Generated by Django 4.0 on 2022-04-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0008_alter_typeofmodeling_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, verbose_name='Имя ответа')),
                ('answer', models.CharField(default=None, max_length=100, verbose_name='ответ 5')),
            ],
            options={
                'verbose_name': 'Модель ответа',
                'verbose_name_plural': 'Модели ответов',
                'ordering': ['id'],
            },
        ),
    ]