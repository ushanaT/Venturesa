# Generated by Django 4.2.2 on 2023-12-18 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vent', '0005_delete_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=7)),
                ('refered_by', models.CharField(max_length=20)),
            ],
        ),
    ]