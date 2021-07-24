from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('example/', csrf_exempt(views.example)),
    path('organization/', csrf_exempt(views.organization))
]