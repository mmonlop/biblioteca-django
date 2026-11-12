from django.shortcuts import render
from .models import Libro
from django.db.models import Q  

# Create your views here.
def principal(request):

    consultas = Libro.objects.filter(
        Q(precio__gt=10) &  Q(titulo__icontains= 'django')
        )

    for libro in consultas:
        print(libro)

    libro = Libro.objects.all().filter(id=1).update(titulo="Nuevo titulo")
    return render(request, 'principal.html')