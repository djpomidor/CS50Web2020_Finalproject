# Generated by Django 4.0.2 on 2022-08-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0004_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(blank=True, choices=[(None, 'Select...'), ('BK', 'Book'), ('CL', 'Calendar'), ('MZ', 'Magazine'), ('NP', 'Newspaper'), ('FL', 'Flyers')], max_length=2),
        ),
        migrations.AlterField(
            model_name='paper',
            name='type',
            field=models.CharField(choices=[(None, 'Select...'), ('GL', 'Glossy'), ('MAT', 'Matte'), ('OFF', 'Offset')], max_length=3),
        ),
        migrations.AlterField(
            model_name='part',
            name='color',
            field=models.CharField(blank=True, choices=[(None, 'Select...'), ('4_4', '4+4'), ('4_0', '4+0')], max_length=3),
        ),
        migrations.AlterField(
            model_name='part',
            name='laminate',
            field=models.CharField(blank=True, choices=[(None, 'Select...'), ('MAT', 'Matte'), ('GL', 'Glossy')], max_length=3),
        ),
    ]