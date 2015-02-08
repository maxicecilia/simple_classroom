# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n', blank=True),
            preserve_default=True,
        ),
    ]
