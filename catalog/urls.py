from django.urls import path

from catalog.views import contacts, home, product

urlpatterns = [path('', home), path('contacts/', contacts), path('product/<int:pk>/', product)]
