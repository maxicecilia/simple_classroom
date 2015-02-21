# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import simple_classroom.apps.downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('data', models.FileField(storage=simple_classroom.apps.downloads.DropboxStorageDeconstructible(), null=True, upload_to=b'files', blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
                ('assignment', models.ForeignKey(to='classroom.Assignment')),
            ],
            options={
                'verbose_name': 'Descarga',
                'verbose_name_plural': 'Descargas',
            },
            bases=(models.Model,),
        ),
    ]
