# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foo',
            old_name='bar',
            new_name='bar2',
        ),
        migrations.AlterIndexTogether(
            name='foo',
            index_together=set([('foo', 'bar2')]),
        ),
    ]
