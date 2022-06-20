from django.db import models
from contatos.models import Contato
from django import forms


# Create your models here.


class FormsContato(forms.ModelForm):
    class Meta:
        model  = Contato
        exclude = ()
    