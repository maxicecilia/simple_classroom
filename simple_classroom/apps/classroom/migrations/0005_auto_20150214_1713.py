# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20150214_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentprofile',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='teacherprofile',
            options={'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='avatar',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'avatar', null=True, verbose_name='Avatar', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='site',
            field=models.ForeignKey(verbose_name='Sitio', to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='user',
            field=models.OneToOneField(verbose_name='Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
