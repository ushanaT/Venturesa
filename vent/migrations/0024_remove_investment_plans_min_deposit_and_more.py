# Generated by Django 4.2.2 on 2023-12-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vent', '0023_alter_accounts_acctb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment_plans',
            name='min_deposit',
        ),
        migrations.AlterField(
            model_name='coin_rate',
            name='bitcoin',
            field=models.CharField(default=2.3e-05, max_length=10000),
        ),
        migrations.AlterField(
            model_name='investment_plans',
            name='duration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='withdrawals',
            name='accountnumber',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawals',
            name='amount',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawals',
            name='status',
            field=models.CharField(default='Request Accepted: Processing', max_length=1000),
        ),
    ]
