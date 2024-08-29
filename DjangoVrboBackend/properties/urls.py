from django.urls import path
from . import api

urlpatterns = [
    path('', api.property_list, name = "api_property_list"),
    path('api/properties', include('properties.api.urls')),
]