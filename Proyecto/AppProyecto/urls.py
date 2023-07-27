from django.urls import path
from AppProyecto.views import *
from . import views
from .views import UsuarioEdicion
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.home, name="home"),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('logout/', LogoutView.as_view(template_name='AppProyecto/logout.html'), name='logout'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('ventaCreacion/', VentaCreacion.as_view(), name='nuevo'),
    path('autoDetalle/', autoDetalle.as_view(), name='auto'),
]