from django.contrib import admin
from django.urls import path
from web import views as view_web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_web.home, name="home"),
    path('unidade/<int:unit_id>/', view_web.unit_detail, name='unit_detail'),
    path('inscrever/<int:unit_id>/', view_web.subscribe_to_the_unit, name='subscribe_to_the_unit'),
]