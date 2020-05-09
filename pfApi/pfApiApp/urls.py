from django.urls import path

from . import views

urlpatterns = [
    path('labels', views.getLabels, name='labels')
]
