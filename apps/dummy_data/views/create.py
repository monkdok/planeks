from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect, render
from apps.dummy_data.forms import SchemaForm
from apps.dummy_data.forms.column import ColumnsFormset
from apps.dummy_data.models import Column
from apps.dummy_data.utils import formset_validation


@login_required
def create(request):
    context = {}
    form = SchemaForm(request.POST or None)
    formset = ColumnsFormset(
        request.POST or None,
        queryset=Column.objects.none(),
    )
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                formset_validation(request, form, formset)
            except IntegrityError:
                raise IntegrityError("Error Encountered")
            return redirect('dummy_data:schema_list')
    context['formset'] = formset
    context['form'] = form
    return render(request, 'dummy_data/create_schema.html', context)
