from django.db import models
import django
from django.utils import timezone
# Create your models here.

class CatalogEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"

    catalog_engine_code = models.CharField(max_length=255, verbose_name="Catalog Engine Code",  null=False, editable=False, unique=True)
    core_engine_code = models.CharField(max_length=255, verbose_name="Core Engine Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=128, verbose_name="User Tenant Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    module_code = models.CharField(max_length=255, verbose_name="Module Code", null=False, editable=False)
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
    io_engine_details = models.TextField(verbose_name="IO Engine Details")
    core_engine_details = models.TextField(verbose_name="Core Engine Details")
    is_activated = models.BooleanField(default=False, verbose_name="Is Activated ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class CatalogEngineActivations(models.Model):
    class meta:
        db_table = "engine_activations"

    catalog_engine = models.ForeignKey(CatalogEngine, verbose_name="Catalog Engine", on_delete=models.CASCADE)
    core_engine_code = models.CharField(max_length=255, verbose_name="Core Engine Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=128, verbose_name="User Tenant Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    module_code = models.CharField(max_length=255, verbose_name="Module Code", null=False, editable=False)
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

class ParentGroup(models.Model):
    class Meta:
        db_table = "parent_group"

    group_code = models.CharField(max_length=255, verbose_name="Group Code", null=False, editable=False)
    user_group_code = models.CharField(max_length=128, verbose_name="User Group Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=128, verbose_name="User Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    group_name = models.CharField(max_length=255, verbose_name="Group Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Entities(models.Model):
    class Meta:
        db_table = "entities"

    parent_group = models.ForeignKey(ParentGroup, verbose_name="Parent Group", on_delete=models.CASCADE)
    entity_code = models.CharField(max_length=255, verbose_name="Entity Code", null=False, editable=False)
    user_entity_code = models.CharField(max_length=128, verbose_name="User Entity Code", null=False, editable=False)
    group_code = models.CharField(max_length=255, verbose_name="Group Code", null=False, editable=False)
    user_group_code = models.CharField(max_length=255, verbose_name="User Group Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=255, verbose_name="User Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    entity_name = models.CharField(max_length=255, verbose_name="Entity Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class Division(models.Model):
    class Meta:
        db_table = "division"

    parent_group = models.ForeignKey(ParentGroup, verbose_name="Parent Group", on_delete=models.CASCADE)
    entity = models.ForeignKey(Entities, verbose_name="Entity", on_delete=models.CASCADE)
    division_code = models.CharField(max_length=255, verbose_name="Division Code", null=False, editable=False)
    user_division_code = models.CharField(max_length=255, verbose_name="User Division Code", null=False, editable=False)
    entity_code = models.CharField(max_length=255, verbose_name="Entity Code", null=False, editable=False)
    user_entity_code = models.CharField(max_length=128, verbose_name="User Entity Code", null=False, editable=False)
    group_code = models.CharField(max_length=255, verbose_name="Group Code", null=False, editable=False)
    user_group_code = models.CharField(max_length=255, verbose_name="User Group Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=255, verbose_name="User Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    division_name = models.CharField(max_length=255, verbose_name="Division Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class EntityLocation(models.Model):
    class Meta:
        db_table = "entity_location"

    entity = models.ForeignKey(Entities, verbose_name="Entity", on_delete=models.CASCADE)
    address_type = models.CharField(max_length=48, verbose_name="Address Type", choices=[
        ('H', 'Home'),
        ('O', 'Office')
    ])
    address_line_1 = models.CharField(max_length=255, verbose_name="Address Line1")
    address_line_2 = models.CharField(max_length=255, verbose_name="Address Line2")
    address_line_3 = models.CharField(max_length=255, verbose_name="Address Line3")
    city = models.CharField(max_length=128, verbose_name="City")
    state = models.CharField(max_length=128, verbose_name="State")
    country = models.CharField(max_length=128, verbose_name="Country")
    zip_code = models.CharField(max_length=128, verbose_name="Zip Code")
    is_primary_address = models.BooleanField(default=True, verbose_name="Is Primary Address ?")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class EntityContacts(models.Model):
    class Meta:
        db_table = "entity_contacts"

    entity = models.ForeignKey(Entities, verbose_name="Entity", on_delete=models.CASCADE)
    contact_person_first_name = models.CharField(max_length=64, verbose_name="Contact Person First Name")
    contact_person_last_name = models.CharField(max_length=64, verbose_name="Contact Person Last Name")
    contact_person_designation = models.CharField(max_length=32, verbose_name="Contact Person Designation")
    contact_email = models.EmailField(verbose_name="Contact Email")
    contact_phone_number = models.IntegerField(verbose_name="Contact Phone Number")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class CostCentre(models.Model):
    class Meta:
        db_table = "cost_centre"

    parent_group = models.ForeignKey(ParentGroup, verbose_name="Parent Group", on_delete=models.CASCADE)
    entity = models.ForeignKey(Entities, verbose_name="Entity", on_delete=models.CASCADE)
    division = models.ForeignKey(Division, verbose_name="Division", on_delete=models.CASCADE)
    cost_centre_code = models.CharField(max_length=128, verbose_name="Cost Centre Code", null=False, editable=False)
    division_code = models.CharField(max_length=255, verbose_name="Division Code", null=False, editable=False)
    user_division_code = models.CharField(max_length=128, verbose_name="User Division Code", null=False, editable=False)
    entity_code = models.CharField(max_length=255, verbose_name="Entity Code", null=False, editable=False)
    user_entity_code = models.CharField(max_length=128, verbose_name="User Entity Code", null=False, editable=False)
    group_code = models.CharField(max_length=255, verbose_name="Group Code", null=False, editable=False)
    user_group_code = models.CharField(max_length=255, verbose_name="User Group Code", null=False, editable=False)
    tenant_code = models.CharField(max_length=255, verbose_name="Tenant Code", null=False, editable=False)
    user_tenant_code = models.CharField(max_length=255, verbose_name="User Tenant Code", null=False, editable=False)
    site_code = models.CharField(max_length=255, verbose_name="Site Code", null=False, editable=False)
    instance_code = models.CharField(max_length=255, verbose_name="Instances Code", null=False, editable=False)
    cost_centre_name = models.CharField(max_length=255, verbose_name="Cost Centre Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)

class ShareHoldings(models.Model):
    class Meta:
        db_table = "share_holdings"

    parent_group = models.ForeignKey(ParentGroup, verbose_name="Parent Group", on_delete=models.CASCADE)
    entity = models.ForeignKey(Entities, verbose_name="Entity", on_delete=models.CASCADE)
    entity_code = models.CharField(max_length=255, verbose_name="Entity Code", null=False, editable=False)
    user_entity_code = models.CharField(max_length=128, verbose_name="User Entity Code", null=False, editable=False)
    holder_entity_code = models.CharField(max_length=255, verbose_name="Holder Entity Code")
    holder_user_entity_code = models.CharField(max_length=128, verbose_name="Holder User Entity Code")
    holders_percentage = models.CharField(max_length=32, verbose_name="Holder Percentage")
    is_active = models.BooleanField(default=True, verbose_name="Is Active ?")
    created_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Created On", editable=False)
    last_updated_on = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last Updated On", editable=False)
    last_updated_by = models.CharField(max_length=64, verbose_name="Last Updated By", editable=False)