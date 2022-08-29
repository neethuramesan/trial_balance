# Generated by Django 4.0.2 on 2022-08-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_grunder'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=225)),
                ('group_alias', models.CharField(max_length=225, null=True)),
                ('group_under', models.CharField(max_length=225)),
                ('nature', models.CharField(max_length=255, null=True)),
                ('gross_profit', models.CharField(max_length=255, null=True)),
                ('sub_ledger', models.BooleanField(default=False)),
                ('debit_credit', models.BooleanField(default=False)),
                ('calculation', models.BooleanField(default=False)),
                ('invoice', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]
