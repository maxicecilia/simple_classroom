# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import simple_classroom.apps.downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0006_auto_20150301_2232'),
    ]

    operations = [
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
