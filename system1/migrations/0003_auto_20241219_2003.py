# Generated by Django 3.2 on 2024-12-19 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system1', '0002_auto_20241219_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentmessage',
            name='message_type',
            field=models.CharField(choices=[('sent', 'Sent'), ('received', 'Received')], default='sent', max_length=50),
        ),
        migrations.AlterField(
            model_name='sentmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ReceivedMessage',
        ),
    ]
