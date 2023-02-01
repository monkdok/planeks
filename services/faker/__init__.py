import random
from typing import Callable
from faker import Faker
from faker.providers import person, internet, job, \
    phone_number, address, company, lorem, date_time
from apps.dummy_data.models import Column


class FakeCSV(Faker):
    """Class for generating CSV wih fake data"""
    def __init__(self):
        super().__init__()
        for provider in (person, internet, job, phone_number,
                         address, company, lorem, date_time,):
            self.add_provider(provider)

        # Map data type with Faker library methods
        self._fake_fields = {
            Column.DataType.FULLNAME: self.name,
            Column.DataType.EMAIL: self.ascii_email,
            Column.DataType.PHONE: self.phone_number,
            Column.DataType.ADDRESS: self.phone_number,
            Column.DataType.COMPANY: self.company,
            Column.DataType.JOB: self.job,
            Column.DataType.DOMAIN: self.domain_name,
            Column.DataType.TEXT: self.paragraph,
            Column.DataType.INT: self.random_int,
            Column.DataType.DATE: self.date,
        }

    def get_fake_field(self, column: Column):
        datatype = column.datatype
        field_value = self._fake_fields.get(column.datatype)
        # Call mapped Faker method if it exists
        if field_value and isinstance(field_value, Callable):
            # If no limits call method without parameters
            limits = column.get_limit(datatype)
            if not limits:
                return str(field_value())
            filters = [limit for limit in limits]
            # Assuming only 2 limit parameters are allowed
            params = {filters[0]: random.randrange(column.from_int, column.to_int)} if len(limits) < 2 else \
                {filters[0]: column.from_int, filters[1]: column.to_int}
            # Call Faker method with mapped parameters
            return str(field_value(**params))


