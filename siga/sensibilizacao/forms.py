from django import forms
from sensibilizacao.models import Palestra


class CreatePalestraForm(forms.ModelForm):
    class Meta:
        model = Palestra
        fields = '__all__'
