# Generated by Django 5.0.4 on 2025-01-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
