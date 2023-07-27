from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import FormularioRegistroUsuario, FormularioEdicion,FormularioCambioPassword
from django.views.generic.edit import FormView,UpdateView
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import Vendedor
from .forms import FormularioNuevaVenta
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'AppProyecto/home.html')
class LoginPagina(LoginView):
    template_name = 'AppProyecto/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
class RegistroPagina(FormView):
    template_name = 'AppProyecto/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'AppProyecto/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppProyecto/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')
def password_exitoso(request):
    return render(request, 'AppProyecto/passwordExitoso.html', {})

class VentaCreacion(LoginRequiredMixin, CreateView):
    model = Vendedor
    form_class = FormularioNuevaVenta
    success_url = reverse_lazy('home')
    template_name = 'AppProyecto/ventaCreacion.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VentaCreacion, self).form_valid(form)
    
class autoDetalle(LoginRequiredMixin, DetailView):
    model = Vendedor
    context_object_name = 'auto'
    template_name = 'AppProyecto/autoDetalle.html'