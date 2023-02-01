from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from apps.dummy_data.models import Schema


class SchemaListView(LoginRequiredMixin, ListView):
    template_name = 'dummy_data/schema_list.html'
    model = Schema
    context_object_name = 'schemas'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
