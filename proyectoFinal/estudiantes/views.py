from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.select_related("persona")
    return render(request, "estudiantes/lista.html", {"estudiantes": estudiantes})


def agregar_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_estudiantes")
    else:
        form = EstudianteForm()
    return render(request, "estudiantes/formulario.html", {"form": form})


from django.shortcuts import get_object_or_404


def editar_estudiante(request, estu_id):
    estudiante = get_object_or_404(Estudiante, pk=estu_id)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("lista_estudiantes")
    else:
        form = EstudianteForm(instance=estudiante)
    return render(
        request, "estudiantes/formulario.html", {"form": form, "editar": True}
    )

def eliminar_estudiante(request, estu_id):
    estudiante = get_object_or_404(Estudiante, pk=estu_id)
    if request.method == "POST":
        estudiante.delete()
        return redirect("lista_estudiantes")
    return render(request, "estudiantes/confirmar_eliminar.html", {"estudiante": estudiante}
    )
