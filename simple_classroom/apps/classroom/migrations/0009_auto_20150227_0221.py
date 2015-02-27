# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_auto_20150225_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='site',
            field=models.OneToOneField(to='sites.Site'),
            preserve_default=True,
        ),
    ]
