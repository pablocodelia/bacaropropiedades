from django.db import models

# Create your models here.

class ContactoFormulario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensaje = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre