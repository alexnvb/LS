from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['type', 'date_appointed', 'responsible', 'contractor', 'city', 'forwarder', 'vehicle', 'comment']
        widgets = {
            'type': forms.Select(attrs={"class": "form-control"}),
            'date_appointed': forms.DateTimeInput(attrs={"class": "form-dateinput"}),
            'responsible': forms.Select(attrs={"class": "form-control"}),
            'contractor': forms.Select(attrs={"class": "form-control"}),
            'city': forms.Select(attrs={"class": "form-control"}),
            'forwarder': forms.Select(attrs={"class": "form-control"}),
            'vehicle': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }