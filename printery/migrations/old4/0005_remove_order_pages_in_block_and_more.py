# Generated by Django 4.0.2 on 2022-03-29 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printery', '0004_order_created_alter_order_binding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pages_in_block',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pages_in_cover',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pages_in_insert',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paper_block',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paper_cover',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paper_insert',
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('BLO', 'Block'), ('COV', 'Cover'), ('INS', 'Insert')], max_length=3)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[('4_4', '4+4'), ('4_0', '4+0')], max_length=3)),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printery.order')),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='printery.paper')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='block',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block_order', to='printery.part'),
        ),
        migrations.AddField(
            model_name='order',
            name='cover',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover_order', to='printery.part'),
        ),
        migrations.AddField(
            model_name='order',
            name='insert',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insert_order', to='printery.part'),
        ),
    ]