# Generated by Django 4.0 on 2022-03-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfaAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=500)),
                ('dateOfCreation', models.DateField(auto_now_add=True)),
                ('dateOfChenges', models.DateField(auto_now=True)),
            ],
        ),
    ]
