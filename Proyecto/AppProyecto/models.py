from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
    ArticuloVenta=(
        ("auto","Auto"),
        ("vehiculos","Vehiculos"),
        ("hogar","Hogar"),
        ("electronica","Electronica"),
        ("varios","Varios")
    )
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    articulo=models.CharField(max_length=15, choices=ArticuloVenta, default='auto')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenArticulo = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Vendedor, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)



