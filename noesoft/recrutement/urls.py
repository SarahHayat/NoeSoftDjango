from django.urls import path
from . import views

app_name = 'recrutement'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /recrutement/5/
    path('<int:poste_id>/', views.detail, name='details'),
    path('<int:poste_id>/postuler/', views.postuler, name='postuler'),
]
