# Generated by Django 4.0.2 on 2022-03-20 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0002_rename_owners_order_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner',
            new_name='owners',
        ),
    ]