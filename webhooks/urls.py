from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('organization/', csrf_exempt(views.organization)),
    path('deal/', csrf_exempt(views.deal))
]