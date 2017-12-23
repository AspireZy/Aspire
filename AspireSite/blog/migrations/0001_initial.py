# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-18 23:34
from __future__ import unicode_literals

import blog.models
import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import django_thumbs.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('\u77e5\u8bc6\u5206\u4eab', '\u77e5\u8bc6\u5206\u4eab'), ('\u6280\u672f\u6587\u6863', '\u6280\u672f\u6587\u6863'), ('\u751f\u6d3b\u968f\u7b14', '\u751f\u6d3b\u968f\u7b14'), ('\u6444\u50cf\u827a\u672f', '\u6444\u50cf\u827a\u672f')], default='\u751f\u6d3b\u968f\u7b14', max_length=32, verbose_name='\u7c7b\u522b')),
                ('title', models.CharField(default='title', max_length=32, verbose_name='\u6807\u9898')),
                ('author', models.CharField(default='Aspire.Y', max_length=32, verbose_name='\u4f5c\u8005')),
                ('ArticleIMGname', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('ArticleIMG', django_thumbs.db.models.ImageWithThumbsField(default='\u535a\u5ba2\u56fe\u7247', upload_to=blog.models.generate_filename)),
                ('context', ckeditor.fields.RichTextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fdd\u5b58\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u4fe1\u606f',
                'verbose_name_plural': '\u6587\u7ae0\u4fe1\u606f',
            },
        ),
    ]
