from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    # filtrando tudo
    evento = Evento.objects.all()
    #filtrando pelo usuario
    usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario) -- filtrando pelo usuario
    response = {'evento': evento}
    return render(request,'agenda.html', response)