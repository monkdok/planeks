from django.contrib.auth.models import User
from django.db import models


class BaseDateTime(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Schema(BaseDateTime):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class Column(models.Model):
    class DataType(models.IntegerChoices):
        FULLNAME = 0, 'Full Name'
        EMAIL = 1, 'Email'
        PHONE = 2, 'Phone Number'
        ADDRESS = 3, 'Address'
        COMPANY = 4, 'Company'
        JOB = 5, 'Job Role'
        DOMAIN = 6, 'Domain Name'
        TEXT = 7, 'Text'
        INT = 8, 'Integer'
        DATE = 9, 'Date'

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns', null=True)
    header = models.CharField(max_length=64)
    datatype = models.PositiveSmallIntegerField(
        choices=DataType.choices,
    )
    from_int = models.IntegerField('From', blank=True, null=True)
    to_int = models.IntegerField('To', blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    @classmethod
    def get_limit(cls, datatype):
        """Limit parameters for Faker methods. Map with data type."""
        limits = {
            cls.DataType.TEXT: ('nb_sentences',),
            cls.DataType.INT: ('min', 'max'),
        }
        return limits.get(datatype)


class DataSet(BaseDateTime):
    def get_sub_folder(self, filename):
        return f'datasets/{self.schema.user}/{filename}'

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='datasets')
    file = models.FileField(upload_to=get_sub_folder, blank=True, null=True)
    is_ready = models.BooleanField(default=False)

