from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import Poste, Candidat, Poste_Candidat



def index(request):
    latest_poste_list = Poste.objects.all()
    context = {'latest_poste_list': latest_poste_list}
    return render(request, 'recrutement/index.html', context)


def detail(request, poste_id):
    poste = get_object_or_404(Poste, pk=poste_id)
    return render(request, 'recrutement/details.html', {'poste': poste})


def postuler(request, poste_id):
    poste = get_object_or_404(Poste, pk=poste_id)
    try:
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        cv = request.POST.get('cv')
        telephone = request.POST.get('telephone')
        message = request.POST.get('message')
    except (KeyError, Poste.DoesNotExist):
        return render(request, 'recrutement/details.html', {
            'poste': poste,
            'error_message': "Vous n'avez pas rempli le formulaire.",
        })
    else:
        candidat = Candidat.objects.create(
            prenom=prenom,
            nom=nom,
            email=email,
            cv=cv,
            telephone=telephone,
            message=message,
        )
        candidat.save()
        poste_candidat = Poste_Candidat.objects.create(
            id_candidat=candidat,
            id_poste=poste,
        )
        poste_candidat.save()

        return HttpResponseRedirect(reverse('recrutement:result', args=(poste.id, candidat.id)))


def result(request, poste_id, candidat_id):
    poste = get_object_or_404(Poste, pk=poste_id)
    candidat = get_object_or_404(Candidat, pk=candidat_id)
    return render(request, 'recrutement/result.html', {'poste': poste, 'candidat': candidat})
