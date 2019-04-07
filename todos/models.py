from django.utils.timezone import now

from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    todo = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now, editable=False)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "todos"

