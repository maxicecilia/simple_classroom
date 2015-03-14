# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_auto_20150309_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacherprofile',
            options={'ordering': ('order',), 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
