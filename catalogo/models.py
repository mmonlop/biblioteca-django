from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return super().__str__()


class Editorial(models.Model):
    nombre = models.CharField(max_length=150,unique=True)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return super().__str__()

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


    class Meta:
        ordering = ["titulo"]
        ordering = ["autores"]


    def __str__(self):
        return super().__str__()