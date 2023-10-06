from django.shortcuts import render
from .models import ContactoFormulario
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'index.html')


from .forms import ContactForm

emailempresa = 'pablo.codelia@elevaproductora.cl'

def form_contacto(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']

        contacto = ContactoFormulario(nombre=nombre, email=email, mensaje=mensaje)
        contacto.save()

        # Enviar correo electrónico al interesado
        email_message = EmailMessage(
            subject='Contacto desde bacaroproiedades.cl',
            body=f'Hola, {nombre}. Gracias por contactarte. \n Pronto te hablaremos de vuelta, que tengas un buen día!  .',
            from_email='administrador@bacaropropiedades.cl',
            to = {email},
        )
        print(email_message.subject)
        print(email_message.from_email)
        print(email_message.to)
        print(email_message.body)


        email_message.send()

        # Enviar notificación a MateoSanchez
        email_administrador = EmailMessage(
            subject='Contacto desde bacaroproiedades.cl',
            body=f'Hola, alguien está tratando de contactar desde bacaropropiedades.cl \n \n Nombre: {nombre}\n Correo: {email}\n Mensaje: {mensaje}.\n Devuélveles el mensaje!.',
            from_email='administrador@bacaropropiedades.cl',
            to = {emailempresa},
        )
        print(email_message.subject)
        print(email_message.from_email)
        print(email_message.to)
        print(email_message.body)


        email_administrador.send()



    return render(request, 'registro_cliente.html', {"nombre": contacto.nombre})


""" def form_contacto(request):
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
    # que siempre deben ejecutarse, independientemente de si hay un error o no. """