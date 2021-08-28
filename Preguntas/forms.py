from django import forms
from .models import cuestionario, ElegirRespuesta, respondidas

class elegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(elegirInlineFormset, self).clean()

        respuesta_correcta= 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and formulario.cleaned_data.get("correcta") is True:
                respuesta_correcta += 1

            try:
                assert respuesta_correcta == cuestionario.respuestas_correctas_permitidas

            except AssertionError:
                raise forms.ValidationError("solo se permite una respuesta correcta!")