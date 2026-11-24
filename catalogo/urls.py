from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('editoriales/<int:pk>/',views.editorial_libros, name='editoriales'),
    path('libro/<int:pk>/',views.libros, name='libros'),
    path('autor/<int:pk>/',views.autor, name='autor'),
    path('editoriales/',views.lista_editoriales, name='editorial'),
    path('prestamo/<int:id_libro>/<int:id_usuario>/', views.prestar_libro, name='prestamo'),
    path('devolver/<int:id_libro>', views.devolver_libro,name='devolver')
]