# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateField(null=True, verbose_name='Desde', blank=True)),
                ('date_to', models.DateField(null=True, verbose_name='Hasta', blank=True)),
                ('semester', models.IntegerField(default=1, verbose_name='Semestre', choices=[(1, 'Primero'), (2, 'Segundo')])),
                ('year', models.IntegerField(verbose_name='A\xf1o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=8, verbose_name='C\xf3digo')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=15, null=True, verbose_name='Nombre corto', blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dictation',
            name='subject',
            field=models.ForeignKey(to='classroom.Subject'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='site',
        ),
        migrations.AddField(
            model_name='enrolled',
            name='dictation',
            field=models.ForeignKey(default=0, to='classroom.Dictation'),
            preserve_default=False,
        ),
    ]
