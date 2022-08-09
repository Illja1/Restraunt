from django.contrib import admin

from .models import Lands, Category
class LandsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','content','photo')
    list_display_links= ('id','title')
    search_fields = ('id','title','content')
    list_filter = ('category',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links= ('id','title')
    search_fields = ('title',)
admin.site.register(Lands, LandsAdmin)
admin.site.register(Category, CategoryAdmin)
