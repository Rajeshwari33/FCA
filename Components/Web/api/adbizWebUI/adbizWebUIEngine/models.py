from django.db import models
import django
from django.utils import timezone
# Create your models here.

class AdbizUIEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"

    ui_engine_code = models.CharField(max_length=255, verbose_name="UI Engine Code", null=False, editable=False)
    core_engine_code = models.CharField(max_length=255, verbose_name="Core Engine Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    activation_file_location = models.CharField(max_length=255, verbose_name="Activation File Location")
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    host_name = models.CharField(max_length=128, verbose_name="Host Name")
    host_ip_address = models.GenericIPAddressField(max_length=32, verbose_name="Host IP Address")
    os_release = models.CharField(max_length=32, verbose_name="OS Release")
    release_info = models.CharField(max_length=255, verbose_name="Release Info")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    engine_properties = models.TextField(verbose_name="Engine Properties")
    core_engine_details = models.TextField(verbose_name="Core Engine Details")
    catalog_engine_details = models.TextField(verbose_name="Catalog Engine Details")
    io_engine_details = models.TextField(verbose_name="IO Engine Details")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class AdbizUIEngineActivations(models.Model):
    class Meta:
        db_table = "engine_activations"

    ui_engine_code = models.CharField(max_length=255, verbose_name="UI Engine Code", null=False, editable=False)
    core_engine_code = models.CharField(max_length=255, verbose_name="Core Engine Code", null=False, editable=False)
    activation_key = models.CharField(max_length=255, verbose_name="Activation Key")
    validity_start_date = models.DateTimeField(verbose_name="Validity Start Date")
    validity_end_date = models.DateTimeField(verbose_name="Validity End Date")
    activation_dt = models.DateTimeField(verbose_name="Activation Date")
    deactivation_dt = models.DateTimeField(verbose_name="Deactivation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

