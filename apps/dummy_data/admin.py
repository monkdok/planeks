from django.contrib import admin
from apps.dummy_data.models import Schema, Column, DataSet


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    ...


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    ...


@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    ...
