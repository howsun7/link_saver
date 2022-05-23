from django.urls import path
from .views import index, link_create, category_create

app_name = 'links'

urlpatterns = [
    path('categories/create/', category_create, name='category_create'),
    path('links/add/', link_create, name='link_create'),
    path('', index, name='index'),
]
