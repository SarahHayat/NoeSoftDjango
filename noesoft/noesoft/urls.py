from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('recrutement/', include('recrutement.urls')),
    path('admin/', admin.site.urls),
]