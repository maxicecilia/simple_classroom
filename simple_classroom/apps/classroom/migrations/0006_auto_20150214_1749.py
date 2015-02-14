# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20150214_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='site',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='dictation',
            field=models.ManyToManyField(to='classroom.Dictation', verbose_name='Dictado'),
            preserve_default=True,
        ),
    ]
