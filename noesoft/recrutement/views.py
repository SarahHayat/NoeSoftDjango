from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Poste, Candidat
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
        id = request.get(pk=request.POST['id'])
        prenom = Candidat(request.get(prenom=request.POST['prenom']))
        nom = Candidat(request.get(nom=request.POST['nom']))
        email = Candidat(request.get(prenom=request.POST['email']))
        telephone = Candidat(request.get(prenom=request.POST['telephone']))
        # cv = request.get(prenom=request.POST['cv'])
        message = Candidat(request.get(prenom=request.POST['message']))
    except (KeyError, Poste.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'recrutement/details.html', {
            'poste': poste,
            'error_message': "Vous n'avez pas rempli le formulaire.",
        })
    else:

        prenom.save()
        nom.save()
        email.save()
        telephone.save()
       # cv.save()
        message.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('recrutement:details', args=(poste.id,)))
