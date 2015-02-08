# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_assignment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='evaluation_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de evaluaci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='is_evaluated',
            field=models.BooleanField(default=False, help_text='Tildar para indicar que la evaluaci\xf3n ya fue tomada y est\xe1 disponible.', verbose_name='Evaluado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='is_scored',
            field=models.BooleanField(default=False, help_text='Tildar para indicar que la evaluaci\xf3n ya fue corregida y las notas est\xe1n disponibles.', verbose_name='Corregido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='score_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de Notas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Tildar para mostrar la asignaci\xf3n a los inscriptos.', verbose_name='Publicado'),
            preserve_default=True,
        ),
    ]
