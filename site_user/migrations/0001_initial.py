# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(upload_to='education/images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(upload_to='experience/images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='project/images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(null=True)),
                ('photo', models.ImageField(upload_to='config/images/%Y/%m/%d')),
                ('job_title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('national', models.CharField(max_length=50, null=True)),
                ('languages', models.CharField(max_length=50, null=True)),
                ('biography', models.TextField(max_length=2000)),
                ('about_all', models.TextField(max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('value', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
