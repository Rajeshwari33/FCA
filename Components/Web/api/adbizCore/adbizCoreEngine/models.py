from django.db import models
import django
from django.utils import timezone
# Create your models here.

class Tenants(models.Model):
    class Meta:
        db_table = "tenants"

    product_engine_code = models.CharField(max_length=255, verbose_name="Product Engine Code", null=False, editable=False, unique=True)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False, unique=True)
    user_tenant_code = models.CharField(max_length=128, verbose_name="User Tenant Code", null=False, editable=False, unique=True)
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
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On",
                                           editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated BY", editable=False)

class LicensingInfo(models.Model):
    class Meta:
        db_table = "licensing_info"

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
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class CoreEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"

    core_engine_code = models.CharField(max_length=255, verbose_name="Core Engine Code", null=False, editable=False, unique=True)
    product_engine_code = models.CharField(max_length=255, verbose_name="Product Engine Code", null=False, editable=False, unique=True)
    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    activation_file_location = models.CharField(max_length=255, verbose_name="Activation File Location")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    host_name = models.CharField(max_length=128, verbose_name="Host Name")
    host_ip_address = models.GenericIPAddressField(max_length=32, verbose_name="Host IP Address")
    os_release = models.CharField(max_length=32, verbose_name="OS Release")
    release_info = models.CharField(max_length=255, verbose_name="Release Info")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    product_engine_details = models.TextField(verbose_name="Product Engine Details")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class CoreEngineActivation(models.Model):
    class Meta:
        db_table = "engine_activations"

    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    product_engine_code = models.CharField(max_length=255, verbose_name="Product Engine Code", null=False, editable=False, unique=True)
    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    activation_file_location = models.CharField(max_length=255, verbose_name="Activation File Location")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Sites(models.Model):
    class Meta:
        db_table = "sites"

    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site_code = models.CharField(max_length=255,verbose_name="Site Code", null=False, editable=False)
    site_name = models.CharField(max_length=48, verbose_name="Site Name")
    site_description = models.CharField(max_length=255, verbose_name="Site Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Instances(models.Model):
    class Meta:
        db_table = "instances"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    instance_type = models.CharField(max_length=48, verbose_name="Instance Type")
    instance_description = models.CharField(max_length=255, verbose_name="Instance Description")
    activation_file_location = models.CharField(max_length=255, verbose_name="Activation File Location")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    host_name = models.CharField(max_length=128, verbose_name="Host Name")
    host_ip_address = models.GenericIPAddressField(max_length=32, verbose_name="Host IP Address")
    os_release = models.CharField(max_length=32, verbose_name="OS Release")
    release_info = models.CharField(max_length=255, verbose_name="Release Info")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class InstanceActivation(models.Model):
    class Meta:
        db_table = "instance_activation"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance = models.ForeignKey(Instances, verbose_name="Instances", on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Modules(models.Model):
    class Meta:
        db_table = "modules"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance = models.ForeignKey(Instances, verbose_name="Instances", on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On",  editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Moduleactivations(models.Model):
    class Meta:
        db_table = "module_activations"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance = models.ForeignKey(Instances, verbose_name="Instances", on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, verbose_name="Module", on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class ProcessingEngines(models.Model):
    class Meta:
        db_table = "processing_engines"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance = models.ForeignKey(Instances, verbose_name="Instances", on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, verbose_name="Module", on_delete=models.CASCADE)
    processing_engine_type = models.CharField(max_length=48, verbose_name="Processing Engine Type", choices=[
        ('PE', 'Product Engine'),
        ('CE', 'Core Engine'),
        ('EE', 'ETL Engine'),
        ('IO', 'IO Engine'),
        ('UI', 'WEB UI ENGINE'),
        ('CS', 'Catalog Service')
    ])
    processing_engine_code = models.CharField(max_length=255, verbose_name="Processing Engine Code", null=False,
                                              editable=False, unique=True)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    engine_properties = models.TextField(verbose_name="Engine Properties")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class ProcessingEngineActivations(models.Model):
    class Meta:
        db_table = "processing_engine_activations"

    tenant = models.ForeignKey(Tenants, verbose_name="Tenant", on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, verbose_name="Site", on_delete=models.CASCADE)
    core_engine = models.ForeignKey(CoreEngine, verbose_name="Core Engine", on_delete=models.CASCADE)
    instance = models.ForeignKey(Instances, verbose_name="Instances", on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, verbose_name="Module", on_delete=models.CASCADE)
    processing_engine = models.ForeignKey(ProcessingEngines, verbose_name="Processing Engine", on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)