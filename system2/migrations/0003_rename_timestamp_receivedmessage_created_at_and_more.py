# Generated by Django 5.1.4 on 2024-12-20 02:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system2', '0002_auto_20241219_1551'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='receivedmessage',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='receivedmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
