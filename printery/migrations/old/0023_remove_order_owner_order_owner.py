# Generated by Django 4.0.2 on 2022-03-20 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0022_order_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
