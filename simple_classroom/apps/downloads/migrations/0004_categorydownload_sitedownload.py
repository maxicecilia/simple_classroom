# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import simple_classroom.apps.downloads
import simple_classroom.apps.downloads.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('downloads', '0003_auto_20150225_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('order', models.IntegerField(help_text='De menor a mayor, donde 0 es la primera posicion.', verbose_name='Orden')),
            ],
            options={
                'ordering': ['-order'],
                'verbose_name': 'Categor\xeda',
                'verbose_name_plural': 'Categor\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download_type', models.IntegerField(default=4, verbose_name='Tipo', choices=[(1, 'Diapositivas'), (2, 'Recursos para el alumno'), (3, 'Otros')])),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('data', models.FileField(storage=simple_classroom.apps.downloads.DropboxStorageDeconstructible(location=b'/simple_classroom'), null=True, upload_to=simple_classroom.apps.downloads.models.get_upload_path, blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
                ('category', models.ForeignKey(verbose_name='Categor\xeda', to='downloads.CategoryDownload')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Descarga',
                'verbose_name_plural': 'Descargas',
            },
            bases=(models.Model,),
        ),
    ]
