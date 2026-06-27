from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'asset_id',
                    models.CharField(
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    'asset_name',
                    models.CharField(
                        max_length=100,
                    ),
                ),
                (
                    'category',
                    models.CharField(
                        max_length=50,
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('Available', 'Available'),
                            ('Assigned', 'Assigned'),
                            ('Maintenance', 'Maintenance'),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
