from django.db import models

# Create your models here.
from django.db import models

class Persona(models.Model):
    pers_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

    class Meta:
        db_table = 'persona'
        managed = False  # Para que Django no intente crear la tabla

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(models.Model):
    estu_id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='pers_id')
    codigo_estudiante = models.CharField(max_length=50, unique=True)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'estudiantes'