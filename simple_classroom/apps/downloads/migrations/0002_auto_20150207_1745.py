# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), null=True, upload_to=b'files', blank=True),
            preserve_default=True,
        ),
    ]
