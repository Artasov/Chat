from django import forms

from .models import *


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
