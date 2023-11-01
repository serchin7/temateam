from django.urls import path
from . import views

app_name = 'faults'

urlpatterns = {
    path('', views.tfaults, name='tfaults'),
    path('tAccounts/', views.taccounts, name='taccounts')
}
