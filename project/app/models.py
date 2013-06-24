from django.db import models


class MyModel(models.Model):
    CHAR_FIELD_CHOICES = (("", "Empty Choice"), ('S', "Non Empty Choice"))
    char_field = models.CharField(blank=False, default='', max_length=1,
                                  choices=CHAR_FIELD_CHOICES)
