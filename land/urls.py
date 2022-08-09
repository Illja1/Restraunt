from django.urls import path
from .views import *

urlpatterns = {
    path('', header, name="home"),
    path('cat/<int:category_id>/', get_category, name='category'),
    path('food_menu/<int:category_id>/',get_category, name='food_menu'),
}
