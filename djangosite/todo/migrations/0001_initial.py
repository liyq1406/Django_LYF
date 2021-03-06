# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charactor',
            fields=[
                ('html_id', models.CharField(db_column='html_id', max_length=255, primary_key=True, serialize=False)),
                ('charactor', models.CharField(db_column='charactor', max_length=255)),
                ('hGroup', models.IntegerField(db_column='h_group')),
            ],
            options={
                'db_table': '20171024_charactor_ceshi',
                'managed': 'False',
            },
        ),
        migrations.CreateModel(
            name='TodoEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('create_date', models.DateTimeField(verbose_name='create date')),
            ],
            options={
                'db_table': '20171024_todoentry_ceshi',
                'managed': 'False',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('html_id', models.CharField(db_column='html_id', max_length=255, primary_key=True, serialize=False)),
                ('userName', models.CharField(db_column='username', max_length=200)),
                ('passWord', models.CharField(db_column='password', max_length=200)),
                ('cid', models.IntegerField(db_column='cid')),
            ],
            options={
                'db_table': '20171024_user_ceshi',
                'managed': 'False',
            },
        ),
    ]
