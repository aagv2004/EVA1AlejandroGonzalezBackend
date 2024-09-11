from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, ('eva1app/index.html'))

def vistaPostre1(request):
    postre = {
        "nombrePostre1":"Torta Pampodour",
        "descripcionPostre1": "Torta de crema y manjar",
    }
    return render(request, ('eva1app/postre.html'), postre)

def vistaPostre2(request):
    postre = {
        "nombrePostre2":"Brazo de Reina",
        "descripcionPostre2":"Bizcocho con manjar espolvoreado de azucar flor",
    }
    return render(request, ('eva1app/postre.html'), postre)

def vistaPostre3(request):
    postre = {
        "nombrePostre3":"Queque",
        "descripcionPostre3":"Bizcocho de molde redondo",
    }
    return render(request, ('eva1app/postre.html'), postre)
