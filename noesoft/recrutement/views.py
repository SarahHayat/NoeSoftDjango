from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Poste, Candidat, Poste_Candidat
from django.template import loader


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
        # Redisplay the question voting form.
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


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('recrutement:details', args=(poste.id,)))
