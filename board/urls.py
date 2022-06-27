from django.urls import  path
from . import  views

urlpatterns=[
    path('list/',views.list , name='list'),
    path('view/',views.view , name='view'),
    path('write/',views.write , name='write'),
    path('remove/',views.remove , name='remove'),
    path('modify/',views.modify , name='modify'),
]