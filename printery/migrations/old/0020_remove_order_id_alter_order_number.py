# Generated by Django 4.0.2 on 2022-03-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0019_delete_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
