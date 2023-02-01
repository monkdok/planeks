from django import forms
from apps.dummy_data.models import Schema


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }
