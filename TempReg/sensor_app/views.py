from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewReading, SearchReading, RegistroForm, ReadSensor
from .models import Lectura

def index(request):
    title = "Temp Reg"
    return render(request, "index.html", {
        "title": title
    })

def lista_lecturas(request):
    lectura = Lectura.objects.all().order_by('-fecha')[:10]
    return render(request, 'lista_lecturas.html', {'lecturas': lectura})

def agregar_lecturas(request):
    if request.method == "GET":
        return render(request, 'agregar_lectura.html', {
            "forms": CreateNewReading()
        })
    else:
        fecha = request.POST['fecha']
        valor = request.POST['valor']
        ubicacion = request.POST['ubicacion']
        Lectura.objects.create(fecha=fecha, valor=valor, ubicacion=ubicacion)
        return redirect('lista_lecturas')

def eliminar_lecturas(request, pk):
    print(pk)
    registro = get_object_or_404(Lectura, pk=pk)
    if request.method == "POST":
        registro.delete()
        return redirect('buscar_lecturas')
    return render(request, 'eliminar_lectura.html', {'registro': registro})

def modificar_lecturas(request, pk):
    print(pk)
    registro = get_object_or_404(Lectura, pk=pk)
    if request.method == "POST":
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('buscar_lecturas')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'form_lectura.html', {'form': form})

def buscar_lectura(request):
    mensaje = ""
    registro = None
    if request.method == "POST":
        form = SearchReading(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            try:
                registro = Lectura.objects.filter(fecha=fecha)
                print(registro)
            except Lectura.DoesNotExist:
                mensaje = "No se encontró un registro con esa fecha."
    else:
        form = SearchReading()
    return render(request, 'buscar_lectura.html', {'form': form, 'registro': registro, 'mensaje': mensaje})

def leer_dato_Pi(request):
    if request.method == "GET":
        return render(request, 'sensor_read.html', {
            "forms": ReadSensor()
        })
    else:
        fecha = request.POST['fecha']
        valor = request.POST['valor']
        ubicacion = request.POST['ubicacion']
        Lectura.objects.create(fecha=fecha, valor=valor, ubicacion=ubicacion)
        return redirect('lista_lecturas')