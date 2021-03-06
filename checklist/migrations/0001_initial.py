# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-15 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(blank=True, default='', max_length=30)),
                ('tags', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todotask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(blank=True, max_length=120, null=True)),
                ('tick', models.BooleanField(default=False)),
                ('checklist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='checklist.Checklist')),
            ],
        ),
    ]
