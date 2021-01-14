from django.db import models
import django
from django.utils import timezone
from djchoices import choices

# Create your models here.

class ProductEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"

    product_engine_code = models.CharField(max_length=255, verbose_name="Product Engine Code", null=False, editable=False, unique=True)
    registered_to = models.CharField(max_length=64, verbose_name="Registered To")
    activation_file_location = models.CharField(max_length=255, verbose_name="Activation File Location")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    host_name = models.CharField(max_length=128, verbose_name="Host Name")
    host_ip_address = models.GenericIPAddressField(max_length=32, verbose_name="Host IP Address")
    os_release = models.CharField(max_length=32, verbose_name="OS Release")
    release_info = models.CharField(max_length=255, verbose_name="Release Info")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Tenants(models.Model):
    class Meta:
        db_table = "tenants"

    product_engine = models.ForeignKey(ProductEngine, verbose_name="Product Engine", on_delete=models.CASCADE)
    tenant_code = models.CharField(max_length=255,verbose_name="Tenant Code", null=False, editable=False, unique=True)
    tenant_name = models.CharField(max_length=64, verbose_name="Tenant Name")
    registration_number = models.CharField(max_length=32, verbose_name="Registration Number")
    registration_dt = models.DateTimeField(verbose_name="Registration Date")
    company_category = models.CharField(max_length=48, verbose_name="Company Category", choices=[
        ('PROP', 'Proprietorship'),
        ('OPC', 'One Person Company'),
        ('PTNR', 'Traditional Partnership'),
        ('LLLP', 'Limited Liability Partnership (LLP)'),
        ('PVT', 'Private Limited Company')
    ])
    company_sub_category = models.CharField(max_length=48, verbose_name="Company Sub Catagory", choices=[
        ('PROP', 'Proprietorship'),
        ('OPC', 'One Person Company'),
        ('PTNR', 'Traditional Partnership'),
        ('LLLP', 'Limited Liability Partnership (LLP)'),
        ('PVT', 'Private Limited Company')
    ])
    company_type = models.CharField(max_length=48, verbose_name="Company Type", choices=[
        ('L', 'Listed'),
        ('U', 'Unlisted')
    ])
    city = models.CharField(max_length=32, verbose_name="City")
    state_code = models.CharField(max_length=3, verbose_name="State Code")
    country_code = models.CharField(max_length=3, verbose_name="Country Code")
    website_url = models.CharField(max_length=128, verbose_name="Website Url")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated BY", editable=False)

class TenantContactDetails(models.Model):
    class Meta:
        db_table = "tenant_contact_details"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    contact_person_first_name = models.CharField(max_length=48, verbose_name="Contact Person First Name")
    contact_person_last_name = models.CharField(max_length=48, verbose_name="Contact Person Last Name")
    contact_person_designation = models.CharField(max_length=48, verbose_name="Contact Person Designation")
    contact_email = models.EmailField(verbose_name="Contact Email")
    contact_phone_code = models.IntegerField(verbose_name="Contact Phone Code")
    contact_phone_number = models.IntegerField(verbose_name="Contact Phone Number")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class TenantLocations(models.Model):
    class Meta:
        db_table = "tenant_locations"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    address_type = models.CharField(max_length=48, verbose_name="Address Type", choices=[
        ('H', 'Home'),
        ('O', 'Office')
    ])
    address_line_1 = models.CharField(max_length=128, verbose_name="Address Line1")
    address_line_2 = models.CharField(max_length=128, verbose_name="Address Line2")
    address_line_3 = models.CharField(max_length=128, verbose_name="Address Line3")
    country_code = models.CharField(max_length=3, verbose_name="Country Code")
    city = models.CharField(max_length=32, verbose_name="City")
    state_code = models.CharField(max_length=3, verbose_name="State Code")
    zip_code = models.CharField(max_length=3, verbose_name="Zip Code")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class LicensingInfo(models.Model):
    class Meta:
        db_table = "licensing_info"

    product_engine = models.ForeignKey(ProductEngine, verbose_name="Product Engine", on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    license_type = models.CharField(max_length=48, verbose_name="License Type", choices=[
        ('SUBCRPTN', 'Subscription Based'),
        ('PRPTL', 'Perpetual'),
        ('EVAL', 'Evaluation')
    ])
    license_key = models.CharField(max_length=55, verbose_name="License Key")
    duration_days = models.PositiveIntegerField(verbose_name="Duration Days")
    active_modules = models.CharField(max_length=255, verbose_name="Active Modules")
    active_engines = models.CharField(max_length=255, verbose_name="Active Engines")
    active_environments = models.CharField(max_length=255, verbose_name="Actve Environments")
    active_from_dt = models.DateTimeField(verbose_name="Active From Date")
    active_end_dt = models.DateTimeField(verbose_name="Active End Date")
    activated_on_dt = models.DateTimeField(verbose_name="Activated On Date")
    deactivated_on_dt = models.DateTimeField(verbose_name="Deactivated On Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By",editable=False)

class LicenseParameters(models.Model):
    class Meta:
        db_table = "license_parameters"
    license = models.ForeignKey(LicensingInfo, verbose_name="License", on_delete=models.CASCADE)
    product_edition = models.CharField(max_length=64, verbose_name="Product Edition")
    storage_engine = models.CharField(max_length=64, verbose_name="Storage Engine")
    chart_library = models.CharField(max_length=64, verbose_name="Chart Library")
    table_library = models.CharField(max_length=64, verbose_name="Table Library")
    default_period_months = models.SmallIntegerField(verbose_name="Default Period Months")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On",editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class LicenseSiteActivations(models.Model):
    class Meta:
        db_table = "license_site_activations"

    license = models.ForeignKey(LicensingInfo, verbose_name="License", on_delete=models.CASCADE)
    site = models.CharField(max_length=255, verbose_name="Site")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class LicenseInstanceActivations(models.Model):
    class Meta:
        db_table = "license_instance_activations"

    license = models.ForeignKey(LicensingInfo, verbose_name="License", on_delete=models.CASCADE)
    instance_type = models.CharField(max_length=48, verbose_name="Instance Type")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class LicenseEngineActivations(models.Model):
    class Meta:
        db_table = "license_engine_activation"

    license = models.ForeignKey(LicensingInfo, verbose_name="License", on_delete=models.CASCADE)
    site = models.CharField(max_length=255, verbose_name="Site")
    instance_type = models.CharField(max_length=48, verbose_name="Instance Type")
    processing_engine_type = models.CharField(max_length=48, verbose_name="Processing Engine Type", choices=[
        ('PE', 'Product Engine'),
        ('CE', 'Core Engine'),
        ('EE', 'ETL Engine'),
        ('IO', 'IO Engine'),
        ('UI', 'WEB UI ENGINE'),
        ('CS', 'Catalog Service')
    ])
    processing_engine_code = models.CharField(max_length=255, verbose_name="Processing Engine Code", null=False, editable=False, unique=True)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class LicenseModuleActivations(models.Model):
    class Meta:
        db_table = "license_module_activations"

    license = models.ForeignKey(LicensingInfo, verbose_name="License", on_delete=models.CASCADE)
    site = models.CharField(max_length=255, verbose_name="Site")
    instance_type = models.CharField(max_length=48, verbose_name="Instance Type")
    module = models.CharField(max_length=48, verbose_name="Module", choices=[
        ('ACTPBL', 'ACCOUNT PAYABLES'),
        ('ACTRBL', 'ACCOUNT RECEIVABLES'),
        ('BANK_RECO', 'BANK_RECONCILIATIONS')
    ])
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

