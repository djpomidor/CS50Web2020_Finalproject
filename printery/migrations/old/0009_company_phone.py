# Generated by Django 4.0.2 on 2022-02-28 16:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0008_alter_company_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None, unique=True),
            preserve_default=False,
        ),
    ]
