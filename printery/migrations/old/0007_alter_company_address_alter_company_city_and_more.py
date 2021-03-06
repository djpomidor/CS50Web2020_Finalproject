# Generated by Django 4.0.2 on 2022-02-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0006_rename_is_employee_user_is_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, max_length=56),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.IntegerField(blank=True),
        ),
    ]
