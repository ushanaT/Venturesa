# Generated by Django 4.2.2 on 2023-12-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vent', '0017_deposit_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_account_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctn', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Coin_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitcoin', models.IntegerField(default=2.3e-05)),
            ],
        ),
        migrations.AddField(
            model_name='deposit_request',
            name='bitcoin_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
