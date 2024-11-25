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

def dia_da_semana(request, numero):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia = dias.get(numero, "Dia inválido")
    return render(request, "dia_da_semana.html", {'numero': numero, 'dia': dia})

def dashboard(request):
    return render(request, 'dashboard.html')
