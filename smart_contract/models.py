from django.db import models


class SmartContract(models.Model):
    sender = models.CharField(max_length=42)
    newName = models.CharField(max_length=127)
