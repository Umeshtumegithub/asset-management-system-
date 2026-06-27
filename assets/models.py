from django.db import models


class Asset(models.Model):
    asset_id = models.CharField(
        max_length=20,
        unique=True
    )

    asset_name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50
    )

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Maintenance', 'Maintenance'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.asset_name
