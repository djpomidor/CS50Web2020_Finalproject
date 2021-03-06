# Generated by Django 4.0.2 on 2022-03-20 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0024_remove_order_owner_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order_owners', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
