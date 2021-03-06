# Generated by Django 3.1.4 on 2021-01-14 05:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Product Engine Code')),
                ('registered_to', models.CharField(max_length=64, verbose_name='Registered To')),
                ('activation_file_location', models.CharField(max_length=255, verbose_name='Activation File Location')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('host_name', models.CharField(max_length=128, verbose_name='Host Name')),
                ('host_ip_address', models.GenericIPAddressField(verbose_name='Host IP Address')),
                ('os_release', models.CharField(max_length=32, verbose_name='OS Release')),
                ('release_info', models.CharField(max_length=255, verbose_name='Release Info')),
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
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Tenant Code')),
                ('tenant_name', models.CharField(max_length=64, verbose_name='Tenant Name')),
                ('registration_number', models.CharField(max_length=32, verbose_name='Registration Number')),
                ('registration_dt', models.DateTimeField(verbose_name='Registration Date')),
                ('company_category', models.CharField(choices=[('PROP', 'Proprietorship'), ('OPC', 'One Person Company'), ('PTNR', 'Traditional Partnership'), ('LLLP', 'Limited Liability Partnership (LLP)'), ('PVT', 'Private Limited Company')], max_length=48, verbose_name='Company Category')),
                ('company_sub_category', models.CharField(choices=[('PROP', 'Proprietorship'), ('OPC', 'One Person Company'), ('PTNR', 'Traditional Partnership'), ('LLLP', 'Limited Liability Partnership (LLP)'), ('PVT', 'Private Limited Company')], max_length=48, verbose_name='Company Sub Catagory')),
                ('company_type', models.CharField(choices=[('L', 'Listed'), ('U', 'Unlisted')], max_length=48, verbose_name='Company Type')),
                ('city', models.CharField(max_length=32, verbose_name='City')),
                ('state_code', models.CharField(max_length=3, verbose_name='State Code')),
                ('country_code', models.CharField(max_length=3, verbose_name='Country Code')),
                ('website_url', models.CharField(max_length=128, verbose_name='Website Url')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated BY')),
                ('product_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.productengine', verbose_name='Product Engine')),
            ],
            options={
                'db_table': 'tenants',
            },
        ),
        migrations.CreateModel(
            name='TenantLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('H', 'Home'), ('O', 'Office')], max_length=48, verbose_name='Address Type')),
                ('address_line_1', models.CharField(max_length=128, verbose_name='Address Line1')),
                ('address_line_2', models.CharField(max_length=128, verbose_name='Address Line2')),
                ('address_line_3', models.CharField(max_length=128, verbose_name='Address Line3')),
                ('country_code', models.CharField(max_length=3, verbose_name='Country Code')),
                ('city', models.CharField(max_length=32, verbose_name='City')),
                ('state_code', models.CharField(max_length=3, verbose_name='State Code')),
                ('zip_code', models.CharField(max_length=3, verbose_name='Zip Code')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'tenant_locations',
            },
        ),
        migrations.CreateModel(
            name='TenantContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_first_name', models.CharField(max_length=48, verbose_name='Contact Person First Name')),
                ('contact_person_last_name', models.CharField(max_length=48, verbose_name='Contact Person Last Name')),
                ('contact_person_designation', models.CharField(max_length=48, verbose_name='Contact Person Designation')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact Email')),
                ('contact_phone_code', models.IntegerField(verbose_name='Contact Phone Code')),
                ('contact_phone_number', models.IntegerField(verbose_name='Contact Phone Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'tenant_contact_details',
            },
        ),
        migrations.CreateModel(
            name='LicensingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(choices=[('SUBCRPTN', 'Subscription Based'), ('PRPTL', 'Perpetual'), ('EVAL', 'Evaluation')], max_length=48, verbose_name='License Type')),
                ('license_key', models.CharField(max_length=55, verbose_name='License Key')),
                ('duration_days', models.PositiveIntegerField(verbose_name='Duration Days')),
                ('active_modules', models.CharField(max_length=255, verbose_name='Active Modules')),
                ('active_engines', models.CharField(max_length=255, verbose_name='Active Engines')),
                ('active_environments', models.CharField(max_length=255, verbose_name='Actve Environments')),
                ('active_from_dt', models.DateTimeField(verbose_name='Active From Date')),
                ('active_end_dt', models.DateTimeField(verbose_name='Active End Date')),
                ('activated_on_dt', models.DateTimeField(verbose_name='Activated On Date')),
                ('deactivated_on_dt', models.DateTimeField(verbose_name='Deactivated On Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('product_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.productengine', verbose_name='Product Engine')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'licensing_info',
            },
        ),
        migrations.CreateModel(
            name='LicenseSiteActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, verbose_name='Site')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.licensinginfo', verbose_name='License')),
            ],
            options={
                'db_table': 'license_site_activations',
            },
        ),
        migrations.CreateModel(
            name='LicenseParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_edition', models.CharField(max_length=64, verbose_name='Product Edition')),
                ('storage_engine', models.CharField(max_length=64, verbose_name='Storage Engine')),
                ('chart_library', models.CharField(max_length=64, verbose_name='Chart Library')),
                ('table_library', models.CharField(max_length=64, verbose_name='Table Library')),
                ('default_period_months', models.SmallIntegerField(verbose_name='Default Period Months')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.licensinginfo', verbose_name='License')),
            ],
            options={
                'db_table': 'license_parameters',
            },
        ),
        migrations.CreateModel(
            name='LicenseModuleActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, verbose_name='Site')),
                ('instance_type', models.CharField(max_length=48, verbose_name='Instance Type')),
                ('module', models.CharField(choices=[('ACTPBL', 'ACCOUNT PAYABLES'), ('ACTRBL', 'ACCOUNT RECEIVABLES'), ('BANK_RECO', 'BANK_RECONCILIATIONS')], max_length=48, verbose_name='Module')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.licensinginfo', verbose_name='License')),
            ],
            options={
                'db_table': 'license_module_activations',
            },
        ),
        migrations.CreateModel(
            name='LicenseInstanceActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_type', models.CharField(max_length=48, verbose_name='Instance Type')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.licensinginfo', verbose_name='License')),
            ],
            options={
                'db_table': 'license_instance_activations',
            },
        ),
        migrations.CreateModel(
            name='LicenseEngineActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, verbose_name='Site')),
                ('instance_type', models.CharField(max_length=48, verbose_name='Instance Type')),
                ('processing_engine_type', models.CharField(choices=[('PE', 'Product Engine'), ('CE', 'Core Engine'), ('EE', 'ETL Engine'), ('IO', 'IO Engine'), ('UI', 'WEB UI ENGINE'), ('CS', 'Catalog Service')], max_length=48, verbose_name='Processing Engine Type')),
                ('processing_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Processing Engine Code')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizProductEngine.licensinginfo', verbose_name='License')),
            ],
            options={
                'db_table': 'license_engine_activation',
            },
        ),
    ]
