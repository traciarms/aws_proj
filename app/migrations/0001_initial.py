# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('reason', models.CharField(max_length=250)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Team')),
            ],
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
