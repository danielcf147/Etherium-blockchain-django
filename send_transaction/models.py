from django.db import models


class Transaction(models.Model):
    sender = models.CharField(max_length=42)
    recipient = models.CharField(max_length=42)
    value_sent = models.IntegerField()
