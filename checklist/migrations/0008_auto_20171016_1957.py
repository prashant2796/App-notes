# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-16 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0007_auto_20171016_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customtags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_tag', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='checklist',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Wk/Of', 'Work/Office'), ('Hm', 'Home'), ('Sc/Co', 'School/College'), ('Ho', 'Hobby')], max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='customtags',
            name='checklist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='custom_tags', to='checklist.Checklist'),
        ),
    ]
