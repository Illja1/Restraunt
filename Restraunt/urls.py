from django.contrib import admin
from django.urls import path
from land import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start_page, name='home'),
    path('menu/' ,views.Menu, name='menu'),
    path('cat/<int:category_id>/' ,views.get_category, name='category'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
