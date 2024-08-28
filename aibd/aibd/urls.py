from django.contrib import admin
from django.urls import path
from web import views as view_web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_web.home, name="home"),
]