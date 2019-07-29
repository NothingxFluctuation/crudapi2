from django.db import models
from django.utils import timezone
# Create your models here.


DATABASE_TYPE: tuple = (
    ('ORACLE','ORACLE_DB'),
    ('SYBASE','SYBASE_DB'),

)


class SimpleModel(models.Model):
    name = models.CharField(max_length = 500, unique = True)
    description = models.TextField(max_length=2000, null=True, blank = True)
    driver = models.CharField(max_length=20,choices=DATABASE_TYPE)
    host = models.CharField(max_length=100)
    port = models.IntegerField()
    username = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.name