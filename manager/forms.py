# forms.py
from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["date", "name", "item", "location", "phone_number", "time_in"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "border rounded p-2 w-full"}),
            "name": forms.TextInput(attrs={"class": "border rounded p-2 w-full", "placeholder": "Dr. John Doe"}),
            "item": forms.TextInput(attrs={"class": "border rounded p-2 w-full", "placeholder": "Lenovo Laptop"}),
            "location": forms.TextInput(attrs={"class": "border rounded p-2 w-full", "placeholder": "Room 1"}),
            "phone_number": forms.TextInput(attrs={"class": "border rounded p-2 w-full", "placeholder": "08012345678"}),
            "time_in": forms.TimeInput(attrs={"type": "time", "class": "border rounded p-2 w-full"}),
        }
