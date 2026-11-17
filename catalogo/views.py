from django.shortcuts import render, get_object_or_404
from .models import Libro, Editorial, Autor
from django.db.models import Q, Avg,Sum

# Create your views here.
def principal(request):

    consultas = Libro.objects.filter(
        Q(precio__gt=10) &  Q(titulo__icontains= 'django')
        )

    for libro in consultas:
        print(libro)

    # AGGREGATE
    datos = Libro.objects.aggregate(
        precio_medio = Avg("precio"),
        total_catalogo = Sum("precio")
    )

    libro = Libro.objects.all().filter(id=1).update(titulo="Nuevo titulo")
    return render(request, 'principal.html',{'datos':datos})




def editorial_libros(request,pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    return render(request, 'editorialLibros.html',{'editorial':editorial})

def libros(request,pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalleLibros.html',{'libros':libro})

def autor(request,pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'autor.html',{'autor':autor})

def lista_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request,'editoriales.html',{'editoriales':editoriales})