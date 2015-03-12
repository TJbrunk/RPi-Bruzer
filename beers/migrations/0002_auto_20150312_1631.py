# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='FinalGravity',
            new_name='FG',
        ),
        migrations.RenameField(
            model_name='beer',
            old_name='OriginalGravity',
            new_name='OG',
        ),
    ]
