# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 02:23
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u5185\u5bb9')),
                ('Publish_time', models.CharField(max_length=16, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('Pub_time', models.TimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
        ),
    ]
