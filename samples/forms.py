from django import forms
from . import models

class ObservationForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = models.Observation
        widgets = {
            "sample":forms.HiddenInput()
        }