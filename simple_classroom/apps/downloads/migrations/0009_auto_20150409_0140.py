# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.files.storage
from django.db import models, migrations
import simple_classroom.apps.downloads
import simple_classroom.apps.downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0008_auto_20150314_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={'ordering': ('upload_date',), 'verbose_name': 'Descarga', 'verbose_name_plural': 'Descargas'},
        ),
        migrations.AlterField(
            model_name='download',
            name='data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), null=True, upload_to=b'files', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitedownload',
            name='data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), null=True, upload_to=simple_classroom.apps.downloads.models.get_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
