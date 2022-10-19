from django.urls import path, include

urlpatterns = [
    path("auth/",          include("identificacion.urls")),
    path("profile/",       include("perfiles.urls")),
    path("admin/",         include("administracion.urls")),
    path("files/",         include("archivos.urls")),
    path("departamentos/", include("departamentos.urls")),
]
