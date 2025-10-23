from django.db import models


# Tabla models de Equipo
class Equipo(models.Model):

    #Variables para almacenar las tuplas que voy a designar mas adelante en choices
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

    #Atributos definidos con model
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='')
    estado = models.CharField(max_length=50, choices=ESTADO, default='operativo')
    fecha_ingreso = models.DateField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)

    #Función str para obtener
    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - {self.estado}"
