# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20150203_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictation',
            options={'verbose_name': 'Dictado', 'verbose_name_plural': 'Dictados'},
        ),
        migrations.AlterModelOptions(
            name='enrolled',
            options={'verbose_name': 'Inscripto', 'verbose_name_plural': 'Inscriptos'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Materia', 'verbose_name_plural': 'Materias'},
        ),
        migrations.AddField(
            model_name='dictation',
            name='is_registration_open',
            field=models.BooleanField(default=True, verbose_name='Registraci\xf3n abierta'),
            preserve_default=True,
        ),
    ]
