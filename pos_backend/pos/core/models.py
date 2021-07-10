from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.reverse_related import OneToOneRel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categoria(models.Model):
    categoria_nom = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria_nom

class Mesa(models.Model):
    mesa_nro    = models.IntegerField
    mesa_cap    = models.IntegerField
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class Plato(models.Model):
    plato_pre   = models.FloatField()
    plato_nom   = models.CharField(max_length=50)
    plato_img   = models.ImageField(upload_to="platos")
    categoria   = models.ForeignKey(Categoria, on_delete=CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    email =models.EmailField(unique=True)
    usu_nom = models.CharField(max_length=50)
    usu_ape = models.CharField(max_length=50)
    usu_tipo = models.CharField(max_length=45)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email']

class Pedido(models.Model):
    pedido_fecha = models.DateTimeField()
    pedido_nro = models.CharField(max_length=10)
    pedido_est = models.CharField(max_length=20)
    mesa = models.ForeignKey(Mesa, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    platos = models.ManyToManyField(Plato, through='PedidoPlato')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class PedidoPlato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=CASCADE)
    plato = models.ForeignKey(Plato, on_delete=CASCADE)
    pedidoplato_cant = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)