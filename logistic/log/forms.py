from django import forms
from django.forms import DateInput
from django.utils import formats
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NewsForm(forms.ModelForm):


    class Meta:
        model = Record
        fields = ['type', 'date_appointed', 'responsible', 'contractor', 'city', 'forwarder', 'vehicle', 'comment']
        widgets = {
            'type': forms.Select(attrs={"class": "form-control"}),
            'date_appointed': DateInput(),
            'responsible': forms.Select(attrs={"class": "form-control"}),
            'contractor': forms.Select(attrs={"class": "form-control"}),
            'city': forms.Select(attrs={"class": "form-control"}),
            'forwarder': forms.Select(attrs={"class": "form-control"}),
            'vehicle': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }