# Generated by Django 3.2.6 on 2021-08-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_device_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authenticate',
            old_name='totop',
            new_name='totp',
        ),
    ]
