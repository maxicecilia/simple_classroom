# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.files.storage
from django.db import models, migrations
import simple_classroom.apps.downloads


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_auto_20150207_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), null=True, upload_to=b'files', blank=True),
            preserve_default=True,
        ),
    ]
