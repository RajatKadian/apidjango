from django.db import models

# Create your models here.

class Info(models.Model):
    document_name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    port = models.IntegerField(null=True)
    ip_address = models.GenericIPAddressField(null=True)

