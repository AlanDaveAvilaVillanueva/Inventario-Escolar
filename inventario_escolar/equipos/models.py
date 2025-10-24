from django.db import models


# Tabla models de Equipo
class Equipo(models.Model):

    #Variables para almacenar las tuplas que voy a designar mas adelante en choices
    ESTADO = [
        ('operativo', 'Operativo'),
        ('en_reparacion', 'En Reparación'),
        ('dado_de_baja', 'Dado de Baja')

    ]

    #Atributos definidos con model
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='categorias')
    estado = models.CharField(max_length=50, choices=ESTADO, default='operativo')
    fecha_ingreso = models.DateField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)

    #Función str para obtener
    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - {self.estado}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}
