# Generated by Django 3.1.4 on 2021-01-14 06:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Core Engine Code')),
                ('product_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Product Engine Code')),
                ('activation_file_location', models.CharField(max_length=255, verbose_name='Activation File Location')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('host_name', models.CharField(max_length=128, verbose_name='Host Name')),
                ('host_ip_address', models.GenericIPAddressField(verbose_name='Host IP Address')),
                ('os_release', models.CharField(max_length=32, verbose_name='OS Release')),
                ('release_info', models.CharField(max_length=255, verbose_name='Release Info')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('product_engine_details', models.TextField(verbose_name='Product Engine Details')),
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
            name='Instances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('instance_type', models.CharField(max_length=48, verbose_name='Instance Type')),
                ('instance_description', models.CharField(max_length=255, verbose_name='Instance Description')),
                ('activation_file_location', models.CharField(max_length=255, verbose_name='Activation File Location')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('host_name', models.CharField(max_length=128, verbose_name='Host Name')),
                ('host_ip_address', models.GenericIPAddressField(verbose_name='Host IP Address')),
                ('os_release', models.CharField(max_length=32, verbose_name='OS Release')),
                ('release_info', models.CharField(max_length=255, verbose_name='Release Info')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
            ],
            options={
                'db_table': 'instances',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.instances', verbose_name='Instances')),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Product Engine Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Tenant Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=128, unique=True, verbose_name='User Tenant Code')),
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
            ],
            options={
                'db_table': 'tenants',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('site_name', models.CharField(max_length=48, verbose_name='Site Name')),
                ('site_description', models.CharField(max_length=255, verbose_name='Site Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'sites',
            },
        ),
        migrations.CreateModel(
            name='ProcessingEngines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_engine_type', models.CharField(choices=[('PE', 'Product Engine'), ('CE', 'Core Engine'), ('EE', 'ETL Engine'), ('IO', 'IO Engine'), ('UI', 'WEB UI ENGINE'), ('CS', 'Catalog Service')], max_length=48, verbose_name='Processing Engine Type')),
                ('processing_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Processing Engine Code')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('engine_properties', models.TextField(verbose_name='Engine Properties')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Is Activated ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.instances', verbose_name='Instances')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.modules', verbose_name='Module')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'processing_engines',
            },
        ),
        migrations.CreateModel(
            name='ProcessingEngineActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.instances', verbose_name='Instances')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.modules', verbose_name='Module')),
                ('processing_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.processingengines', verbose_name='Processing Engine')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'processing_engine_activations',
            },
        ),
        migrations.AddField(
            model_name='modules',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site'),
        ),
        migrations.AddField(
            model_name='modules',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant'),
        ),
        migrations.CreateModel(
            name='Moduleactivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.instances', verbose_name='Instances')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.modules', verbose_name='Module')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'module_activations',
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
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'licensing_info',
            },
        ),
        migrations.AddField(
            model_name='instances',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site'),
        ),
        migrations.AddField(
            model_name='instances',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant'),
        ),
        migrations.CreateModel(
            name='InstanceActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.instances', verbose_name='Instances')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.sites', verbose_name='Site')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'instance_activation',
            },
        ),
        migrations.CreateModel(
            name='CoreEngineActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Product Engine Code')),
                ('activation_file_location', models.CharField(max_length=255, verbose_name='Activation File Location')),
                ('activation_key', models.CharField(max_length=255, verbose_name='Activation Key')),
                ('validity_start_date', models.DateTimeField(verbose_name='Validity Start Date')),
                ('validity_end_date', models.DateTimeField(verbose_name='Validity End Date')),
                ('activation_dt', models.DateTimeField(verbose_name='Activation Date')),
                ('deactivation_dt', models.DateTimeField(verbose_name='Deactivation Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('core_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.coreengine', verbose_name='Core Engine')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant')),
            ],
            options={
                'db_table': 'engine_activations',
            },
        ),
        migrations.AddField(
            model_name='coreengine',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCoreEngine.tenants', verbose_name='Tenant'),
        ),
    ]