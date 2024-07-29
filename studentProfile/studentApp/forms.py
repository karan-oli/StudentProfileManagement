from django import forms
from .models import Class

class ClassSelectionForm(forms.Form):
    selected_class = forms.ModelChoiceField(queryset=Class.objects.all())
