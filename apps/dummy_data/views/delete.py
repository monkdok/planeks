from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from apps.dummy_data.models import Column, Schema


class DeleteModelInstanceAjax:
    """Custom view for deleting Schema or Column instances"""

    # Map kwargs with Model
    MODELS = {
        'schema': Schema,
        'column': Column,
    }

    @classmethod
    def delete_instance(cls, request, *args, **kwargs):
        model = kwargs.get('model')
        pk = int(kwargs.get('pk'))
        if not pk or pk is None:
            # It means that there is not saved instance and front may safely remove
            # html element.
            return
        try:
            instance = get_object_or_404(cls.MODELS.get(model), pk=int(pk))
        except Http404:
            return JsonResponse({'error': 'Object Does not exit'})
        instance.delete()
        if model == 'schema':
            # Schema model handle with regular HTTP request
            return HttpResponseRedirect(reverse_lazy('dummy_data:schema_list'))
        # Column model handle with AJAX(HTTP) request
        return JsonResponse({'success': 'Object deleted successfully'})


