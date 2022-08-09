from django.db import models


class Lands(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name="Info")
    photo = models.ImageField(upload_to='photos/&Y/%m/&d/', verbose_name='Photo',blank=True)
    category = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, blank=True )

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = "Food menu "
        verbose_name_plural= "Foods menu"

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Food category")

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = "Food category "
        verbose_name_plural= "Foods categories"
