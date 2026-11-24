from django.db import models
from django.db.models import Q
from django.conf import settings

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Editorial(models.Model):
    nombre = models.CharField(max_length=150,unique=True)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    class Genero(models.TextChoices):
        NOVELA = "NOV", "Novela"
        POESIA = "POE", "Poesía"
        TEATRO = "TEA", "Teatro"
        ENSAYO = "ENS", "Ensayo"
        COMIC = "COM", "Cómic"

    genero = models.CharField(
        max_length=3,
        choices=Genero.choices,
        default=Genero.NOVELA,
    )

    class Dificultad(models.IntegerChoices):
        BASICA = 1, "Básica"
        INTERMEDIA = 2, "Intermedia"
        AVANZADA = 3, "Avanzada"

    dificultad = models.IntegerField(
        choices=Dificultad.choices,
        default=Dificultad.BASICA,
    )

    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13,unique=True)
    sinopsis = models.TextField(blank=True)
    fecha_publicacion = models.DateField()
    paginas = models.PositiveBigIntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    disponible = models.BooleanField(default=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, related_name="libros",null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name="libros",null=True,blank=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        constraints = [
            models.CheckConstraint(
                condition=Q(precio__gte=0),
                name="precio_libro_negativo"
            )
        ]


    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(
        "Libro", on_delete=models.PROTECT,
        related_name="prestamos"
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="prestamos_biblioteca"
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo {self.pk}: {self.libro}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre