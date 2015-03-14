# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0007_auto_20150309_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorydownload',
            options={'ordering': ['order'], 'verbose_name': 'Categor\xeda', 'verbose_name_plural': 'Categor\xedas'},
        ),
    ]
