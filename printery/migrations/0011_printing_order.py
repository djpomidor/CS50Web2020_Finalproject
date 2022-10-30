# Generated by Django 4.0.2 on 2022-09-28 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0010_remove_printing_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='printing',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printery.order', to_field='number'),
        ),
    ]