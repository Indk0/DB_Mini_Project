from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('collectornotes', views.collectors_notes, name='notes'),
    path('customertransactions', views.customer_transaction, 
         name='transactions'),
    path('plans', views.plans, name='plans'),
]
