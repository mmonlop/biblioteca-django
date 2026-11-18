# from django.shortcuts import render, get_object_or_404
# from .models import Libro, Editorial, Autor
# from django.db.models import Q, Avg,Sum,Count

# # Create your views here.
# def principal(request):

#     # consultas = Libro.objects.filter(
#     #     Q(precio__gt=10) &  Q(titulo__icontains= 'django')
#     #     )

#     # for libro in consultas:
#     #     print(libro)

#     # # AGGREGATE
#     # datos = Libro.objects.aggregate(
#     #     precio_medio = Avg("precio"),
#     #     total_catalogo = Sum("precio")
#     # )

#     # libro = Libro.objects.all().filter(id=1).update(titulo="Nuevo titulo")


#     #Recupera todos los libros de una editorial.
#     editorial = Editorial.objects.first()

#     libros = editorial.libros.all()


    
#     #Recupera todos los libros de un autor.

#     autor = Autor.objects.first()

#     libros_autor = autor.libros.all()

#     #Recupera todos los autores de un libro.

#     autor_libro = Libro.objects.first()

#     autores_de_libro = autor_libro.autores.all()


#     #Muestra el número de libros por editorial mediante annotate()

#     total_libros_editorial = Editorial.objects.filter(pk=editorial.pk).annotate(
#         total=Count("libros")
#     )


#     # Recupera los libros desde una editorial y desde un autor utilizando related_name






#     return render(request, 'principal.html', {'libros':libros, 'libros_autor':libros_autor, 'editorial': editorial, 'autor':autor, 'autores_d_libro':autores_de_libro,
#                                               'libro':autor_libro, 'total_libros':total_libros_editorial})







# def editorial_libros(request,pk):
#     editorial = get_object_or_404(Editorial, pk=pk)
#     return render(request, 'editorialLibros.html',{'editorial':editorial})

# def libros(request,pk):
#     libro = get_object_or_404(Libro, pk=pk)
#     return render(request, 'detalleLibros.html',{'libros':libro})

# def autor(request,pk):
#     autor = get_object_or_404(Autor, pk=pk)
#     return render(request, 'autor.html',{'autor':autor})

# def lista_editoriales(request):
#     editoriales = Editorial.objects.all()
#     return render(request,'editoriales.html',{'editoriales':editoriales})