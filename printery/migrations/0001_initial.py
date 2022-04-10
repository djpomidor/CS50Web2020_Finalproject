# Generated by Django 4.0.2 on 2022-03-30 17:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import printery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_employee', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(blank=True, max_length=64)),
                ('city', models.CharField(blank=True, max_length=25)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=56)),
                ('email', models.CharField(blank=True, max_length=64)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('is_manufacturer', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=printery.models.Order.counter, unique=True)),
                ('name', models.CharField(blank=True, max_length=16)),
                ('type', models.CharField(blank=True, choices=[(None, ''), ('BK', 'Book'), ('CL', 'Calendar'), ('MZ', 'Magazine'), ('NP', 'Newspaper'), ('FL', 'Flyers')], max_length=2)),
                ('circulation', models.IntegerField(blank=True, null=True)),
                ('binding', models.CharField(blank=True, choices=[(None, 'Select...'), ('GLU', 'Glue'), ('STA', 'Staple'), ('HAR', 'Hardcover'), ('FOL', 'Folding')], max_length=4)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ManyToManyField(blank=True, related_name='order_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('GL', 'Glossy'), ('MAT', 'Matte'), ('OFF', 'Offset')], max_length=3)),
                ('density', models.IntegerField(choices=[(80, '80 gr/m2'), (120, '120 gr/m2'), (150, '150 gr/m2'), (200, '200 gr/m2'), (250, '250 gr/m2')])),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('manufacturer', models.ManyToManyField(blank=True, related_name='made_by', to='printery.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(blank=True, choices=[('BLO', 'Block'), ('COV', 'Cover'), ('INS', 'Insert')], max_length=3)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[('4_4', '4+4'), ('4_0', '4+0')], max_length=3)),
                ('laminate', models.CharField(blank=True, choices=[('MAT', 'Matte'), ('GL', 'Glossy')], max_length=3)),
                ('uflak', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printery.order')),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='printery.paper')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printery.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
