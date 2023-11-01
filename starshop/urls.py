
from django.urls import path 
from .views import star_create, star_detail, checkout
from . import views
urlpatterns=[
    path("", views.hp , name='hp'),
    path("lab/", views.lab , name='lab'),
    path("lab/createstar/", star_create.as_view(), name='star_create'),
    path("<str:name>/<str:createdBy>/", star_detail , name='star_detail'),
    path("<str:name>/<str:createdBy>/checkout", checkout.as_view() , name='checkout'),
]
