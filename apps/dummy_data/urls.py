from django.urls import path
from apps.dummy_data.views.create import create
from apps.dummy_data.views.delete import DeleteModelInstanceAjax
from apps.dummy_data.views.detail import SchemaDetailView
from apps.dummy_data.views.generate import generate_dataset_ajax, create_dataset_ajax
from apps.dummy_data.views.list import SchemaListView
from apps.dummy_data.views.update import SchemaUpdateView

app_name = 'dummy_data'

urlpatterns = [
    path('', SchemaListView.as_view(), name='schema_list'),
    path('create-schema/', create, name='create_schema'),
    path('update-schema/<pk>', SchemaUpdateView.as_view(), name='update_schema'),
    path('delete/<model>/<pk>', DeleteModelInstanceAjax.delete_instance, name='delete'),
    path('schema/<pk>', SchemaDetailView.as_view(), name='detail_schema'),
    path('create-dataset/<pk>', create_dataset_ajax, name='create_dataset'),
    path('generate/<pk>', generate_dataset_ajax, name='generate'),
]


