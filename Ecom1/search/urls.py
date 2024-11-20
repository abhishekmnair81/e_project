from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('searchproducts/', views.searchproducts, name='search'),


]