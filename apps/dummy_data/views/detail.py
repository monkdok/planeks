from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from apps.dummy_data.models import Schema


class SchemaDetailView(LoginRequiredMixin, DetailView):
    model = Schema
    template_name = 'dummy_data/detail_schema.html'
    context_object_name = 'schema'
