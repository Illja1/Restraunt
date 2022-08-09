# Generated by Django 4.0.3 on 2022-05-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_alter_lands_options_alter_lands_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Food category')),
            ],
            options={
                'verbose_name': 'Food category ',
                'verbose_name_plural': 'Foods categories',
            },
        ),
        migrations.AddField(
            model_name='lands',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='land.category'),
        ),
    ]
