import csv
from io import StringIO
from django.core.files.base import ContentFile
from services.faker import FakeCSV


# @shared_task()
def generate_csv(schema, rows_num, dataset):
    faker = FakeCSV()
    schema_name = schema.name
    schema_columns = schema.columns.all()
    headers = (column.header for column in schema_columns)
    rows = ([faker.get_fake_field(column) for column in schema_columns] for _ in range(int(rows_num)))
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(headers)
    writer.writerows(rows)
    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
    dataset.file.save(f'{schema_name}.csv', csv_file)
    dataset.is_ready = True
    dataset.save()
