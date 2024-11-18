from django.shortcuts import render # type: ignore

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

#view exibir_item
def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id':id})
#view perfil
def perfil(request, usuario):
    return render(request, "perfil.html", {'usuario':usuario})

