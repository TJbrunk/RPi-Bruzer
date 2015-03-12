# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('BrewDate', models.DateField(unique=True)),
                ('OriginalGravity', models.DecimalField(max_digits=4, decimal_places=3)),
                ('Notes', models.TextField(blank=True)),
                ('RackDate', models.DateField(null=True, blank=True)),
                ('FinishDate', models.DateField(null=True, blank=True)),
                ('FinalGravity', models.DecimalField(null=True, max_digits=4, decimal_places=3, blank=True)),
                ('ABV', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('OnTap', models.BooleanField(default=False)),
                ('FermentationTemp', models.PositiveSmallIntegerField(default=18)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BeerTempData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Temperature', models.DecimalField(max_digits=5, decimal_places=2)),
                ('Brew', models.ForeignKey(to='beers.Beer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
