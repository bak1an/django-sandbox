from django.db import models


class Foo(models.Model):
    foo = models.IntegerField()
    bar2 = models.IntegerField(default=42)

    class Meta:
        index_together = (('foo', 'bar2'), )
