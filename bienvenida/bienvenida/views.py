from django.http import HttpResponse

def inicio(request):
    nombre = "Cesar Silva"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")