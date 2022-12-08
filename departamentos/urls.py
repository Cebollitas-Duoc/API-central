from django.urls import path
from . import views

app_name = "departamentos"

urlpatterns = [
    path('viewdptos/',                  views.ViewDptos,     name="ViewDptos"),
    path('viewfotosdpto/<int:idDpto>/', views.ViewFotosDpto, name="ViewFotosDpto"),
    path('viewdpto/<int:idDpto>/',      views.ViewDpto,      name="ViewDpto"),
    
    path('listservices/<int:idDpto>/',      views.listServices,               name="listServices"),
    path('listservicecategories/',          views.listServiceCategories,      name="listServiceCategories"),
    path('listextraservices/<int:idDpto>/', views.listExtraServices,          name="listExtraServices"),
    path('listextraservicecategories/',     views.listExtraServiceCategories, name="listExtraServiceCategories"),

    path('listWorkers/', views.listWorkers, name="listWorkers"),
]