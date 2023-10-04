from django.shortcuts import render
from .models import ContactoFormulario

# Create your views here.
def index(request):
    return render(request, 'index.html')



def form_contacto(request):
    try:
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Realiza la validación de los datos si es necesario

        contacto = ContactoFormulario(nombre=nombre, email=email, mensaje=mensaje)
        contacto.save()

        # Realiza cualquier acción adicional que necesites después de guardar

        return render( request, 'registro_cliente.html', {"nombre": contacto.nombre})
    except Exception as e:
        # Manejo de errores: puedes personalizar este mensaje de acuerdo a tus necesidades
        error_message = "Ha ocurrido un error durante el envío de datos."

        # Puedes imprimir el error en la consola para depuración
        print(f"Error: {str(e)}")

        # Puedes renderizar una página de error o redirigir a una página específica
        return render(request, 'error.html', {'error_message': error_message})

    # Opcionalmente, podrías también considerar un bloque finally para acciones finales
    # que siempre deben ejecutarse, independientemente de si hay un error o no.