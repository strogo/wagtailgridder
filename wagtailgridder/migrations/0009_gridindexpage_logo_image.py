# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailgridder', '0008_auto_20170320_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridindexpage',
            name='logo_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
