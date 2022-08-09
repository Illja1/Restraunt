# Generated by Django 4.0.3 on 2022-05-24 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_category_lands_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lands',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='land.category'),
        ),
        migrations.AlterField(
            model_name='lands',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/&Y/%m/&d/', verbose_name='Photo'),
        ),
    ]