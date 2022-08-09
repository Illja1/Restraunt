# Generated by Django 4.0.3 on 2022-05-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0002_rename_menu_lands'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lands',
            options={'verbose_name': 'Food menu ', 'verbose_name_plural': 'Foods menu'},
        ),
        migrations.AlterField(
            model_name='lands',
            name='content',
            field=models.TextField(blank=True, verbose_name='Info'),
        ),
        migrations.AlterField(
            model_name='lands',
            name='photo',
            field=models.ImageField(upload_to='photos/&Y/%m/&d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='lands',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
