from django.urls import path, include

urlpatterns = [
    path("auth/", include("identificacion.urls")),
    path("profile/", include("perfiles.urls")),
]
