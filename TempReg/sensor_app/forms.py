from django import forms
from .models import Lectura

class CreateNewReading(forms.Form):
    fecha = forms.DateTimeField(
        label='Fecha de lectura',
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    valor = forms.FloatField(label='Valor de la lectura')
    ubicacion = forms.CharField(label='Ubicación', max_length=50)

class SearchReading(forms.Form):
    fecha = forms.DateField(label='Fecha de lectura',
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

class ReadSensor(forms.Form):
    fecha = forms.DateTimeField()
    valor = forms.FloatField()
    ubicacion = forms.CharField()

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = ['fecha', 'valor', 'ubicacion']
