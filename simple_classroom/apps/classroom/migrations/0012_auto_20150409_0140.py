# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.files.storage
from django.db import models, migrations
import simple_classroom.apps.downloads


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_auto_20150314_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentprofile',
            options={'ordering': ['user__last_name'], 'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='avatar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'avatar', null=True, verbose_name='Avatar', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='enrolled',
            unique_together=set([('student_profile', 'dictation')]),
        ),
    ]
