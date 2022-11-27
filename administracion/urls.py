from django.urls import path
from . import views

app_name = "administracion"

urlpatterns = [
    path('viewusers/',              views.ViewUsers,          name="ViewUsers"),
    path('edituser/',               views.EditUser,           name="EditUser"),
    path('createdpto/',             views.CreateDpto,         name="CreateDpto"),
    path('editdptos/',              views.EditDpto,           name="EditDpto"),
    path('createfotodpto/',         views.CreateFotoDpto,     name="CreateFotoDpto"),
    path('updatefotodpto/',         views.UpdateFotoDpto,     name="UpdateFotoDpto"),
    path('deletefotodpto/',         views.DeleteFotoDpto,     name="DeleteFotoDpto"),
    path('addservice/',             views.AddService,         name="addService"),
    path('editservice/',            views.EditService,        name="editService"),
    path('addextraservice/',        views.AddExtraService,    name="AddExtraService"),
    path('editextraservice/',       views.EditExtraService,   name="EditExtraService"),
    path('addservicecategory/',     views.AddServiceCategory, name="AddServiceCategory"),
    path('additem/',                views.AddItem,            name="AddItem"),
    path('edititem/',               views.EditItem,           name="EditItem"),
    path('listitems/<int:idItem>/', views.ListItems,          name="ListItems"),
    path('deleteitem/',             views.DeleteItem,          name="DeleteItem"),
]