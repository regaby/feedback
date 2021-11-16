from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = '__all__'
        labels = {
            'nombre': 'Su nombre',
            'opinion': 'Su opinion',
            'puntaje': 'Su puntaje'
        }
        error_messages = {
            'nombre': {
                "required": "su nombre es requerido!",
                "max_length": "por favor ingrese un nombre mas corto"
            }
        }

    # nombre = forms.CharField(
    #     label = "Su nombre",
    #     max_length=100,
    #     error_messages = {
    #         "required": "su nombre es requerido!",
    #         "max_length": "por favor ingrese un nombre mas corto"})
    # opinion = forms.CharField(label="Su opinion", widget=forms.Textarea, max_length=200)
    # puntaje = forms.IntegerField(label="Su puntaje", min_value=1, max_value=5)

