from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Hola amigos esta es mi segunda pagina con Django")
