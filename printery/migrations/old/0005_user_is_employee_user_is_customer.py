# Generated by Django 4.0.2 on 2022-02-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0004_alter_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]
