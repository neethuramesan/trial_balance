# Generated by Django 4.0.5 on 2022-09-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_stock_closingbalance_stock_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockgroup',
            name='closing_balance',
            field=models.IntegerField(null=True),
        ),
    ]
