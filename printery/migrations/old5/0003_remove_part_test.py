# Generated by Django 4.0.2 on 2022-03-29 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0002_part_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='test',
        ),
    ]
