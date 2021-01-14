# Generated by Django 3.1.4 on 2021-01-14 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdbizUIEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ui_engine_code', models.CharField(editable=False, max_length=255, verbose_name='UI Engine Code')),
                ('core_engine_code', models.CharField(editable=False, max_length=255, verbose_name='Core Engine Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('activation_file_location', models.CharField(max_length=255, verbose_name='Activation File Location')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('host_name', models.CharField(max_length=128, verbose_name='Host Name')),
                ('host_ip_address', models.GenericIPAddressField(verbose_name='Host IP Address')),
                ('os_release', models.CharField(max_length=32, verbose_name='OS Release')),
                ('release_info', models.CharField(max_length=255, verbose_name='Release Info')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('engine_properties', models.TextField(verbose_name='Engine Properties')),
                ('core_engine_details', models.TextField(verbose_name='Core Engine Details')),
                ('catalog_engine_details', models.TextField(verbose_name='Catalog Engine Details')),
                ('io_engine_details', models.TextField(verbose_name='IO Engine Details')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
            ],
            options={
                'db_table': 'engine_metadata',
            },
        ),
        migrations.CreateModel(
            name='AdbizUIEngineActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ui_engine_code', models.CharField(editable=False, max_length=255, verbose_name='UI Engine Code')),
                ('core_engine_code', models.CharField(editable=False, max_length=255, verbose_name='Core Engine Code')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
            ],
            options={
                'db_table': 'engine_activations',
            },
        ),
    ]
