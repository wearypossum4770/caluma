# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 14:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("workflow", "0005_auto_20181228_1243")]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="address_groups",
            field=models.TextField(
                blank=True,
                help_text="Group jexl returning what group(s) derived work items will be addressed to.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="workflow",
            name="start",
            field=models.ForeignKey(
                help_text="First task of the workflow.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="workflow.Task",
            ),
        ),
    ]
