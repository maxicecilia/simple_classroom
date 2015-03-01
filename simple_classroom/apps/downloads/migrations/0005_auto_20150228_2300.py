# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0004_categorydownload_sitedownload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedownload',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', blank=True, to='downloads.CategoryDownload', null=True),
            preserve_default=True,
        ),
    ]
