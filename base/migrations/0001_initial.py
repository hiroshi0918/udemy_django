# Generated by Django 4.2 on 2024-08-25 04:31

import base.models.item_models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(default=base.models.item_models.created_id, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('sold_count', models.PositiveIntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='', upload_to=base.models.item_models.upload_image_to)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
                ('tags', models.ManyToManyField(to='base.tag')),
            ],
        ),
    ]
