# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0009_auto_20150227_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ('order',), 'verbose_name': 'Asignaci\xf3n', 'verbose_name_plural': 'Asignaciones'},
        ),
        migrations.AddField(
            model_name='assignment',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='avatar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'avatar', null=True, verbose_name='Avatar', blank=True),
            preserve_default=True,
        ),
    ]
