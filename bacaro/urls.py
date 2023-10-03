
from django.contrib import admin
from django.urls import path
from main import views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.index, name='index'),

    path('form_contacto/', main.form_contacto, name='form_contacto')
]
