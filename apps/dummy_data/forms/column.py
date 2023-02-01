from django import forms
from django.forms import modelformset_factory
from apps.dummy_data.models import Column


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        exclude = ('schema',)
        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'datatype': forms.Select(attrs={'class': 'form-select'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'from_int': forms.NumberInput(attrs={'class': 'form-control'}),
            'to_int': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = super().clean()
        datatype = data.get('datatype')
        from_int = data.get('from_int')
        to_int = data.get('to_int')
        if datatype in (7, 8) and not all((from_int, to_int)):
            self.add_error('datatype', "Fill in 'From' and 'To' fields")
        return data
        
        
ColumnsFormset = modelformset_factory(
    Column,
    form=ColumnForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True
)

