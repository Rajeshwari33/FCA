from django.db import models

# Create your models here.

class ProductEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"