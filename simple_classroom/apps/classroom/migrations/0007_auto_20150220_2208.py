# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20150214_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictation',
            name='dictated_practice_hours',
            field=models.PositiveIntegerField(default=0, verbose_name='Horas dictadas de pr\xe1ctica'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictation',
            name='dictated_theory_hours',
            field=models.PositiveIntegerField(default=0, verbose_name='Horas dictadas de teor\xeda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictation',
            name='last_modification_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de \xfaltima modificaci\xf3n', blank=True),
            preserve_default=True,
        ),
    ]
