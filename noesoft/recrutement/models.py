from django.db import models


class Poste(models.Model):
    titre_poste = models.CharField(max_length=200)
    lieu_poste = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre_poste


class Candidat(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.IntegerField()
    cv = models.FileField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.prenom


class Poste_Candidat(models.Model):
    id_candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    id_poste = models.ForeignKey(Poste, on_delete=models.CASCADE)

