from django.db import IntegrityError
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from apps.dummy_data.forms import SchemaForm
from apps.dummy_data.forms.column import ColumnsFormset
from apps.dummy_data.models import Schema
from django.urls import reverse_lazy
from apps.dummy_data.utils import formset_validation


class SchemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Schema
    form_class = SchemaForm
    formset_class = ColumnsFormset
    template_name = 'dummy_data/create_schema.html'
    success_url = reverse_lazy('dummy_data:schema_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_object().columns.all()
        form = self.form_class(instance=self.get_object())
        formset = self.formset_class(queryset=qs)
        context['formset'] = formset
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(self.model, id=kwargs.get('pk'))
        qs = self.object.columns.all()
        form = SchemaForm(request.POST or None, instance=self.object)
        formset = ColumnsFormset(
            request.POST or None,
            queryset=qs,
        )
        if form.is_valid() and formset.is_valid():
            try:
                formset_validation(request, form, formset)
            except IntegrityError as e:
                raise IntegrityError(f"Error Encount`ered: {e}")
        else:
            return self.get(request, {'form': form, 'formset': formset})
        return redirect(self.success_url)
