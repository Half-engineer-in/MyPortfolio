# Generated by Django 3.2 on 2023-02-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0005_projectshow_projecttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectshow',
            name='desc2',
            field=models.TextField(default='Nothing here'),
            preserve_default=False,
        ),
    ]
