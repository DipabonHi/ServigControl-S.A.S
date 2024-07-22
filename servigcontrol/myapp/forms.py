from django.forms import ModelForm
from .models import Turno

class crear_turno_form(ModelForm):
    class Meta:
        model = Turno
        fields = ['title', 'descripcion']