# Generated by Django 4.2.2 on 2023-12-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vent', '0020_remove_deposit_request_no_deposit_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin_rate',
            name='bitcoin',
            field=models.CharField(default=2.3e-05, max_length=1000),
        ),
    ]
