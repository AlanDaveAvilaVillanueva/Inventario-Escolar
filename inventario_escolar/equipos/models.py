from django.db import models

class Equipo(models.Model):

    CATEGORIAS = [
        ('proyector', 'Proyector'),
        ('notebook', 'Notebook'),
        ('impresora', 'Impresora')
    ]

    ESTADO = [
        ('operativo', 'Operativo'),
        ('en_reparacion', 'En Reparación'),
        ('dado_de_baja', 'Dado de Baja')

    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(choices=CATEGORIAS, default='')
    estado = models.CharField(choices=ESTADO, default='operativo')
    fecha_ingreso = models.DateField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre