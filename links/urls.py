from django.urls import path
from .views import index, link_create

app_name = 'links'

urlpatterns = [
    path('links/add/', link_create, name='create'), 
    path('', index, name='index'),
]
