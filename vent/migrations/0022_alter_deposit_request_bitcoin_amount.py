# Generated by Django 4.2.2 on 2023-12-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vent', '0021_alter_coin_rate_bitcoin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_request',
            name='bitcoin_amount',
            field=models.CharField(max_length=10000),
        ),
    ]