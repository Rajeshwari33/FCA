# Generated by Django 3.1.4 on 2021-01-14 06:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_engine_code', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Catalog Engine Code')),
                ('core_engine_code', models.CharField(editable=False, max_length=255, verbose_name='Core Engine Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=128, verbose_name='User Tenant Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('module_code', models.CharField(editable=False, max_length=255, verbose_name='Module Code')),
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
                ('io_engine_details', models.TextField(verbose_name='IO Engine Details')),
                ('core_engine_details', models.TextField(verbose_name='Core Engine Details')),
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
            name='Entities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_code', models.CharField(editable=False, max_length=255, verbose_name='Entity Code')),
                ('user_entity_code', models.CharField(editable=False, max_length=128, verbose_name='User Entity Code')),
                ('group_code', models.CharField(editable=False, max_length=255, verbose_name='Group Code')),
                ('user_group_code', models.CharField(editable=False, max_length=255, verbose_name='User Group Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=255, verbose_name='User Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('entity_name', models.CharField(max_length=255, verbose_name='Entity Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
            ],
            options={
                'db_table': 'entities',
            },
        ),
        migrations.CreateModel(
            name='ParentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.CharField(editable=False, max_length=255, verbose_name='Group Code')),
                ('user_group_code', models.CharField(editable=False, max_length=128, verbose_name='User Group Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=128, verbose_name='User Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('group_name', models.CharField(max_length=255, verbose_name='Group Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
            ],
            options={
                'db_table': 'parent_group',
            },
        ),
        migrations.CreateModel(
            name='ShareHoldings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_code', models.CharField(editable=False, max_length=255, verbose_name='Entity Code')),
                ('user_entity_code', models.CharField(editable=False, max_length=128, verbose_name='User Entity Code')),
                ('holder_entity_code', models.CharField(max_length=255, verbose_name='Holder Entity Code')),
                ('holder_user_entity_code', models.CharField(max_length=128, verbose_name='Holder User Entity Code')),
                ('holders_percentage', models.CharField(max_length=32, verbose_name='Holder Percentage')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.entities', verbose_name='Entity')),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.parentgroup', verbose_name='Parent Group')),
            ],
            options={
                'db_table': 'share_holdings',
            },
        ),
        migrations.CreateModel(
            name='EntityLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('H', 'Home'), ('O', 'Office')], max_length=48, verbose_name='Address Type')),
                ('address_line_1', models.CharField(max_length=255, verbose_name='Address Line1')),
                ('address_line_2', models.CharField(max_length=255, verbose_name='Address Line2')),
                ('address_line_3', models.CharField(max_length=255, verbose_name='Address Line3')),
                ('city', models.CharField(max_length=128, verbose_name='City')),
                ('state', models.CharField(max_length=128, verbose_name='State')),
                ('country', models.CharField(max_length=128, verbose_name='Country')),
                ('zip_code', models.CharField(max_length=128, verbose_name='Zip Code')),
                ('is_primary_address', models.BooleanField(default=True, verbose_name='Is Primary Address ?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.entities', verbose_name='Entity')),
            ],
            options={
                'db_table': 'entity_location',
            },
        ),
        migrations.CreateModel(
            name='EntityContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_first_name', models.CharField(max_length=64, verbose_name='Contact Person First Name')),
                ('contact_person_last_name', models.CharField(max_length=64, verbose_name='Contact Person Last Name')),
                ('contact_person_designation', models.CharField(max_length=32, verbose_name='Contact Person Designation')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact Email')),
                ('contact_phone_number', models.IntegerField(verbose_name='Contact Phone Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.entities', verbose_name='Entity')),
            ],
            options={
                'db_table': 'entity_contacts',
            },
        ),
        migrations.AddField(
            model_name='entities',
            name='parent_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.parentgroup', verbose_name='Parent Group'),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_code', models.CharField(editable=False, max_length=255, verbose_name='Division Code')),
                ('user_division_code', models.CharField(editable=False, max_length=255, verbose_name='User Division Code')),
                ('entity_code', models.CharField(editable=False, max_length=255, verbose_name='Entity Code')),
                ('user_entity_code', models.CharField(editable=False, max_length=128, verbose_name='User Entity Code')),
                ('group_code', models.CharField(editable=False, max_length=255, verbose_name='Group Code')),
                ('user_group_code', models.CharField(editable=False, max_length=255, verbose_name='User Group Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=255, verbose_name='User Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('division_name', models.CharField(max_length=255, verbose_name='Division Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.entities', verbose_name='Entity')),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.parentgroup', verbose_name='Parent Group')),
            ],
            options={
                'db_table': 'division',
            },
        ),
        migrations.CreateModel(
            name='CostCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_centre_code', models.CharField(editable=False, max_length=128, verbose_name='Cost Centre Code')),
                ('division_code', models.CharField(editable=False, max_length=255, verbose_name='Division Code')),
                ('user_division_code', models.CharField(editable=False, max_length=128, verbose_name='User Division Code')),
                ('entity_code', models.CharField(editable=False, max_length=255, verbose_name='Entity Code')),
                ('user_entity_code', models.CharField(editable=False, max_length=128, verbose_name='User Entity Code')),
                ('group_code', models.CharField(editable=False, max_length=255, verbose_name='Group Code')),
                ('user_group_code', models.CharField(editable=False, max_length=255, verbose_name='User Group Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=255, verbose_name='User Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('cost_centre_name', models.CharField(max_length=255, verbose_name='Cost Centre Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active ?')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created On')),
                ('last_updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Last Updated On')),
                ('last_updated_by', models.CharField(editable=False, max_length=64, verbose_name='Last Updated By')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.division', verbose_name='Division')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.entities', verbose_name='Entity')),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.parentgroup', verbose_name='Parent Group')),
            ],
            options={
                'db_table': 'cost_centre',
            },
        ),
        migrations.CreateModel(
            name='CatalogEngineActivations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_engine_code', models.CharField(editable=False, max_length=255, verbose_name='Core Engine Code')),
                ('user_tenant_code', models.CharField(editable=False, max_length=128, verbose_name='User Tenant Code')),
                ('tenant_code', models.CharField(editable=False, max_length=255, verbose_name='Tenant Code')),
                ('site_code', models.CharField(editable=False, max_length=255, verbose_name='Site Code')),
                ('instance_code', models.CharField(editable=False, max_length=255, verbose_name='Instances Code')),
                ('module_code', models.CharField(editable=False, max_length=255, verbose_name='Module Code')),
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
                ('catalog_engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbizCatalogEngine.catalogengine', verbose_name='Catalog Engine')),
            ],
        ),
    ]
