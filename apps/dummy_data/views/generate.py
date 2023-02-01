import json

from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from apps.dummy_data.models import Schema, DataSet
from apps.dummy_data.tasks import generate_csv


def create_dataset_ajax(request, *args, **kwargs):
    pk = kwargs.get('pk')
    try:
        schema = get_object_or_404(Schema, pk=pk)
    except Http404:
        return JsonResponse({'error': 'Object Does not exit'})
    data_set = DataSet.objects.create(schema=schema)
    return JsonResponse({
        'created_dt': str(data_set.created_dt.strftime('%Y.%m.%d')),
        'dataset_id': data_set.pk,
    })


def generate_dataset_ajax(request, *args, **kwargs):
    data = request.GET.dict()
    data.update(kwargs)
    pk = data.get('pk')
    rows_num = data.get('rows_num')
    dataset_id = data.get('dataset_id')
    try:
        schema = get_object_or_404(Schema, pk=pk)
    except Http404:
        return JsonResponse({'error': 'Object Does not exit'})
    dataset = DataSet.objects.filter(pk=dataset_id).first()
    try:
        generate_csv(schema, rows_num, dataset)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse({'dataset_url': dataset.file.url})

