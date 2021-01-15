from django.forms import ModelForm
from .models import *

from django import forms


class createTémoignages(ModelForm):
    class Meta:
        model = Testimonials
        fields = "testimonials",
