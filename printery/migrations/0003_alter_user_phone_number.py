# Generated by Django 3.2.6 on 2022-01-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0002_auto_20220124_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
