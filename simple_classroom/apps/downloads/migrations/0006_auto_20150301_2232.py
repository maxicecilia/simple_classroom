# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_auto_20150228_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedownload',
            name='download_type',
            field=models.IntegerField(default=4, verbose_name='Tipo', choices=[(0, 'Diapositivas'), (1, 'Recursos para el alumno'), (2, 'Otros')]),
            preserve_default=True,
        ),
    ]
