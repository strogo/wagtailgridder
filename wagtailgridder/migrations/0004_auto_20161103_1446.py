# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('wagtailgridder', '0003_remove_griditem_target_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='griditem',
            old_name='main_image',
            new_name='description_image',
        ),
        migrations.RenameField(
            model_name='griditem',
            old_name='full_desc',
            new_name='description_text',
        ),
        migrations.RenameField(
            model_name='griditem',
            old_name='small_image',
            new_name='summary_image',
        ),
        migrations.RenameField(
            model_name='griditem',
            old_name='summary',
            new_name='summary_text',
        ),
        migrations.AddField(
            model_name='griditem',
            name='landing_page_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
