# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20150207_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='abstract',
            field=tinymce.models.HTMLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
